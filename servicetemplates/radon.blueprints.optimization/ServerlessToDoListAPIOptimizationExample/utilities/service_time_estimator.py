"""Usage: service_time_estimator.py <path to log file>"""
import sys


def main(argv):
    if len(argv) < 1:
        print(__doc__)
        return
    log_filename = argv[0]
    with open(log_filename, "r") as log_file:
        lines = log_file.readlines()
    timestamps = []
    service_times = []
    count = 0
    for l in range(len(lines)):
        left_index = lines[l].find("[")
        right_index = lines[l].find("]")
        if left_index < 0 or right_index < 0:
            continue
        body = lines[l][left_index + 1:right_index].strip()
        if not body[0].isdigit() or not body[-1].isdigit():
            continue
        segments = body.split(", ")
        if not timestamps:
            timestamps = [0 for s in range(len(segments))]
            service_times = [0 for s in range(len(segments) - 1)]
        for s in range(len(segments)):
            timestamps[s] = int(segments[s])
        for s in range(len(segments) - 1):
            service_times[s] += timestamps[s + 1] - timestamps[s]
        count += 1
    for t in range(len(service_times)):
        service_times[t] = round(service_times[t] / count)
    print("Service times: " + str(service_times))

if __name__ == '__main__':
    main(sys.argv[1:])
