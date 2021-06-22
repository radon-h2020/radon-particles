import locust
import random
import threading
import requests
import time
import scipy.stats
import math
import json


API_BASE_URL = 'https://xp48frfnvf.execute-api.eu-central-1.amazonaws.com/production'
THINK_TIME = 1.0
INITIAL_DATA_SET_SIZE = 50
CONFIDENCE_LEVEL = 0.99
MAXIMUM_RELATIVE_ERROR = 0.05


class MyTaskSet(locust.TaskSet):
    wait_function = lambda self: random.expovariate(1 / THINK_TIME) * 1000
    operation_names = ['list_items', 'get_item', 'create_item', 'update_item', 'delete_item']
    operation_distribution = [0.2, 0.4, 0.6, 0.8, 1.0]
    mutex_lock = threading.Lock()
    sampling_complete = False
    sampler_count = 0
    execution_complete = False
    sample_1_sums = [0.0 for i in range(len(operation_names))]
    sample_2_sums = [0.0 for i in range(len(operation_names))]
    sample_counts = [0 for i in range(len(operation_names))]
    relative_errors = [float('inf') for i in range(len(operation_names))]
    item_ids = ['' for i in range(INITIAL_DATA_SET_SIZE)]

    def setup(self):
        MyTaskSet.sampling_complete = False
        MyTaskSet.sampler_count = 0
        MyTaskSet.execution_complete = False
        for i in range(len(MyTaskSet.operation_names)):
            MyTaskSet.sample_1_sums[i] = 0.0
            MyTaskSet.sample_2_sums[i] = 0.0
            MyTaskSet.sample_counts[i] = 0
            MyTaskSet.relative_errors[i] = float('inf')
        response = requests.get(API_BASE_URL + '/todos')
        items = json.loads(response.text)
        if len(items) < INITIAL_DATA_SET_SIZE:
            for i in range(INITIAL_DATA_SET_SIZE - len(items)):
                response = requests.post(API_BASE_URL + '/todos',
                                         json={'todo': 'Have a coffee :-)'})
                item = json.loads(response.text)
                items.append(item)
                time.sleep(1)
        if len(items) > INITIAL_DATA_SET_SIZE:
            for i in range(len(items) - INITIAL_DATA_SET_SIZE):
                item = items.pop(-1)
                requests.delete(API_BASE_URL + '/todos/' + item['id'])
                time.sleep(1)
        MyTaskSet.item_ids = ['' for i in range(INITIAL_DATA_SET_SIZE)]
        for i in range(INITIAL_DATA_SET_SIZE):
            item = items[i]
            MyTaskSet.item_ids[i] = item['id']

    def on_stop(self):
        MyTaskSet._setup_has_run = False

    @locust.task
    def my_task(self):
        if MyTaskSet.execution_complete:
            threading.Event().wait()
        MyTaskSet.mutex_lock.acquire()
        sampling_complete = MyTaskSet.sampling_complete
        if not sampling_complete:
            MyTaskSet.sampler_count += 1
        MyTaskSet.mutex_lock.release()
        random_number = random.random()
        for i in range(len(MyTaskSet.operation_names)):
            if random_number < MyTaskSet.operation_distribution[i]:
                operation_index = i
                break
        operation_name = MyTaskSet.operation_names[operation_index]
        operation_method = getattr(self, operation_name)
        elapsed_time = operation_method(sampling_complete)
        if not sampling_complete:
            MyTaskSet.mutex_lock.acquire()
            MyTaskSet.sample_1_sums[operation_index] += elapsed_time
            MyTaskSet.sample_2_sums[operation_index] += elapsed_time ** 2
            MyTaskSet.sample_counts[operation_index] += 1
            sample_1_sum = MyTaskSet.sample_1_sums[operation_index]
            sample_2_sum = MyTaskSet.sample_2_sums[operation_index]
            sample_count = MyTaskSet.sample_counts[operation_index]
            MyTaskSet.mutex_lock.release()
            if sample_count <= 1:
                relative_error = float('inf')
            else:
                sample_mean = sample_1_sum / sample_count
                sample_variance = (sample_count / (sample_count - 1)) \
                    * (sample_2_sum / sample_count - (sample_1_sum / sample_count) ** 2)
                percent_point = scipy.stats.t.ppf(1 - (1 - CONFIDENCE_LEVEL) / 2, sample_count - 1)
                relative_error = (math.sqrt(sample_variance / sample_count) * percent_point) / sample_mean
            print(operation_name + ': ' + str(relative_error))
            MyTaskSet.mutex_lock.acquire()
            MyTaskSet.relative_errors[operation_index] = relative_error
            sampling_complete = True
            for i in range(len(MyTaskSet.operation_names)):
                if MyTaskSet.relative_errors[i] > MAXIMUM_RELATIVE_ERROR:
                    sampling_complete = False
            if not MyTaskSet.sampling_complete:
                MyTaskSet.sampling_complete = sampling_complete
            MyTaskSet.sampler_count -= 1
            if MyTaskSet.sampling_complete and MyTaskSet.sampler_count <= 0:
                MyTaskSet.execution_complete = True
            MyTaskSet.mutex_lock.release()

    def list_items(self, sampling_complete):
        try:
            start_time = time.time()
            response = requests.get(API_BASE_URL + '/todos')
            if response.status_code != 200:
                raise Exception('Failed to list all the items')
        except Exception as e:
            elapsed_time = time.time() - start_time
            if not sampling_complete:
                locust.events.request_failure.fire(request_type='GET',
                                                   name='list_items',
                                                   response_time=elapsed_time * 1000,
                                                   exception=e)
        else:
            elapsed_time = time.time() - start_time
            if not sampling_complete:
                locust.events.request_success.fire(request_type='GET',
                                                   name='list_items',
                                                   response_time=elapsed_time * 1000,
                                                   response_length=0)
        return elapsed_time

    def get_item(self, sampling_complete):
        MyTaskSet.mutex_lock.acquire()
        item_index = random.randint(0, len(MyTaskSet.item_ids) - 1)
        item_id = MyTaskSet.item_ids.pop(item_index)
        MyTaskSet.mutex_lock.release()
        try:
            start_time = time.time()
            response = requests.get(API_BASE_URL + '/todos/' + item_id)
            if response.status_code != 200:
                raise Exception('Failed to get item: ' + item_id)
        except Exception as e:
            elapsed_time = time.time() - start_time
            if not sampling_complete:
                locust.events.request_failure.fire(request_type='GET',
                                                   name='get_item',
                                                   response_time=elapsed_time * 1000,
                                                   exception=e)
        else:
            elapsed_time = time.time() - start_time
            if not sampling_complete:
                locust.events.request_success.fire(request_type='GET',
                                                   name='get_item',
                                                   response_time=elapsed_time * 1000,
                                                   response_length=0)
        MyTaskSet.mutex_lock.acquire()
        MyTaskSet.item_ids.append(item_id)
        MyTaskSet.mutex_lock.release()
        return elapsed_time

    def create_item(self, sampling_complete):
        try:
            start_time = time.time()
            response = requests.post(API_BASE_URL + '/todos',
                                     json={'todo': 'Have a coffee :-)'})
            if response.status_code != 200:
                raise Exception('Failed to create a new item')
        except Exception as e:
            elapsed_time = time.time() - start_time
            if not sampling_complete:
                locust.events.request_failure.fire(request_type='POST',
                                                   name='create_item',
                                                   response_time=elapsed_time * 1000,
                                                   exception=e)
        else:
            elapsed_time = time.time() - start_time
            if not sampling_complete:
                locust.events.request_success.fire(request_type='POST',
                                                   name='create_item',
                                                   response_time=elapsed_time * 1000,
                                                   response_length=0)
            item = json.loads(response.text)
            MyTaskSet.mutex_lock.acquire()
            MyTaskSet.item_ids.append(item['id'])
            MyTaskSet.mutex_lock.release()
        return elapsed_time

    def update_item(self, sampling_complete):
        MyTaskSet.mutex_lock.acquire()
        item_index = random.randint(0, len(MyTaskSet.item_ids) - 1)
        item_id = MyTaskSet.item_ids.pop(item_index)
        MyTaskSet.mutex_lock.release()
        try:
            start_time = time.time()
            response = requests.put(API_BASE_URL + '/todos/' + item_id,
                                    json={'todo': 'Have a coffee :-)'})
            if response.status_code != 200:
                raise Exception('Failed to update item: ' + item_id)
        except Exception as e:
            elapsed_time = time.time() - start_time
            if not sampling_complete:
                locust.events.request_failure.fire(request_type='PUT',
                                                   name='update_item',
                                                   response_time=elapsed_time * 1000,
                                                   exception=e)
        else:
            elapsed_time = time.time() - start_time
            if not sampling_complete:
                locust.events.request_success.fire(request_type='PUT',
                                                   name='update_item',
                                                   response_time=elapsed_time * 1000,
                                                   response_length=0)
        MyTaskSet.mutex_lock.acquire()
        MyTaskSet.item_ids.append(item_id)
        MyTaskSet.mutex_lock.release()
        return elapsed_time

    def delete_item(self, sampling_complete):
        MyTaskSet.mutex_lock.acquire()
        item_index = random.randint(0, len(MyTaskSet.item_ids) - 1)
        item_id = MyTaskSet.item_ids.pop(item_index)
        MyTaskSet.mutex_lock.release()
        try:
            start_time = time.time()
            response = requests.delete(API_BASE_URL + '/todos/' + item_id)
            if response.status_code != 200:
                raise Exception('Failed to delete item: ' + item_id)
        except Exception as e:
            elapsed_time = time.time() - start_time
            if not sampling_complete:
                locust.events.request_failure.fire(request_type='DELETE',
                                                   name='delete_item',
                                                   response_time=elapsed_time * 1000,
                                                   exception=e)
        else:
            elapsed_time = time.time() - start_time
            if not sampling_complete:
                locust.events.request_success.fire(request_type='DELETE',
                                                   name='delete_item',
                                                   response_time=elapsed_time * 1000,
                                                   response_length=0)
        return elapsed_time


class MyLocust(locust.Locust):
    task_set = MyTaskSet
