#!/usr/bin/python

import json
import random
import string
from sys import argv


class EditTemplate:
    ##In case of development of new datanode, mention the name of node type in "lookup_list" where you want to attach the "on Fail" condition.
    lookup_list = ("S3DataNode", "CopyActivity", "Ec2Resource", "EmrCluster", "EmrActivity", "DynamoDBDataNode",
                   "ShellCommandActivity", "SqlActivity")

    ##in sns_action_def, modify the "role", if you are using custom role definitions
    sns_action_def = {"role": "DataPipelineDefaultRole", "subject": "onFailure Notification", "name": "DefaultAction1",
                      "id": "ActionId_7fFCB",
                      "message": "#{node.errorMessage}", "type": "SnsAlarm", "topicArn":
                          "#{myArnTopic}"}

    sns_ref = {"ref": "ActionId_7fFCB"}

    sns_parameter = {"id": "myArnTopic",
                     "description": "ARN address of the topic, through which we want to send the emails",
                     "type": "String"}


    def read_json_file(self, filename):
        with open(filename) as json_file:
            json_decoded = json.load(json_file)
        return json_decoded

    def add_sns_action(self, json_decoded):
        for key, val in json_decoded.items():
            if key == 'objects':
                val.append(self.sns_action_def)
                for values_0 in val:
                    for sns_nodes in self.lookup_list:
                        if sns_nodes in values_0.values():
                            values_0['onFail'] = self.sns_ref

            if key == 'parameters':
                val.append(self.sns_parameter)
        return json_decoded

    def write_json_file(self, filename, json_decoded):
        a_file = open(filename, "w")
        json.dump(json_decoded, a_file)
        a_file.close()

    ## the function generate an random id and will be attached to "ActionId"
    def generate_id(self):
        res = ''.join(random.sample(string.ascii_letters +
                                    string.digits, k=5))
        return "ActionId_" + res

    def edit_actionId(self, id_val):
        self.sns_action_def['id'] = id_val
        self.sns_ref['ref'] = id_val


if __name__ == "__main__":
    editTemplate = EditTemplate()
    new_id = editTemplate.generate_id()
    editTemplate.edit_actionId(new_id)
    json_content = editTemplate.read_json_file(argv[1])
    modified_json = editTemplate.add_sns_action(json_content)
    editTemplate.write_json_file(argv[1], modified_json)
