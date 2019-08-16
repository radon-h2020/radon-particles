## Kafka Triggers Relationship (OpenWhisk)

OpenWhisk-specific relationship type representing Kafka-to-OpenWhisk Function communication

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `KafkaTriggers` | `radon.relationships.apache.openwhisk.KafkaTriggers` | 1.0.0 | `radon.relationships.abstract.Triggers` |

### Valid Target types

* `radon.capabilities.Invocable`

### Properties

| Name | Required | Type | Constraint | Default Value| Description |
|:---- |:-------- |:---- |:---------- |:-----------  |:----------- |
| `events` | `true` | `list` of `radon.datatypes.Event` | `length: 1` | N/A | A list of events (1 in this case) of type `radon.datatypes.Event` that are conveyed to the target |

### Notes

* Parameters added to the inputs of the `Configure` interface:
    * `EVENT`
    * `TRIGGER_NAME`: needed to correctly create and delete the underlying trigger.
* Parameters added to the inputs of the `Configure` interface operations:
    * `post_configure_target`: `BROKERS`, `TOPIC_NAME`, `IS_JSON_DATA`, `IS_BINARY_KEY`, `IS_BINARY_VALUE`
* The `post_configure_target` operation creates an OpenWhisk trigger based on the Kafka feed, and associates the trigger with the function via a rule.
