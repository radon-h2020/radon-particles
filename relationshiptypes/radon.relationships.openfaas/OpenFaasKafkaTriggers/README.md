## Kafka Triggers Relationship (OpenFaaS)

OpenFaaS-specific relationship type representing Kafka-to-OpenFaaS Function communication

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `OpenFaasKafkaTriggers` | `radon.relationships.openfaas.OpenFaasKafkaTriggers` | 1.0.0 | `radon.relationships.Triggers` |

### Valid Target types

* `radon.capabilities.Invocable`

### Properties

| Name | Required | Type | Constraint | Default Value| Description |
|:---- |:-------- |:---- |:---------- |:-----------  |:----------- |
| `events` | `true` | `list` of `radon.datatypes.Event` | `length: 1` |   | A list of events (1 in this case) of type `radon.datatypes.Event` that are conveyed to the target |

### Notes

* Parameters added to the inputs of the `Configure` interface:
    * `EVENT`
* Parameters added to the inputs of the `Configure` interface operations:
    * `post_configure_target`: `BROKERS`, `TOPIC_NAME`, `GATEWAY_URL`
* The `post_configure_target` operation updates the target function by adding an annotation with the topic name, deploys an OpenFaaS Kafka connector, and configures the connector to forward message from the topic to the function.
