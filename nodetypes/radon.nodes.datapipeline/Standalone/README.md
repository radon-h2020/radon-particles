
## AWS Standalone node type

A node type that represents an AWS Lambda Function.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `PipelineBlock` | `radon.nodes.aws.PipelineBlock` | 1.0.0 | `radon.nodes.abstract.PipelineBlock` |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `pipeline_id` | `string` |   | ID of Pipeline |



### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `dp_name` | `true` | `string` |  |  | Name of the datapipeline to be created |
| `configure_file_path` | `true` | `string` |  |  |  Path of the configuration file |
| `credential_file_path` | `true` | `string` |  |  | Path of the credential file |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.aws.AwsPlatform` | `tosca.relationships.HostedOn`| [1, 1] |


### Notes

* Artifacts:
    * `Create`
    * `Delete`
    * `Start`
    * `Stop`
    * `EditTemplate`: It contains edit_template.py to modify the template file. In case if a new node is added to standalone, there may be some modifications required in edit_template.py. In case if the node name is not present in the "lookup_list", edit the list in the python file, if the user wants "OnFail" notification for a particular node . Also, In case of a user is using the custom roles rather default role, the modification is required to the "role" key which is defined in "sns_action_def" dictionary variable. 


