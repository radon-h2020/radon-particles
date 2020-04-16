## Kafka Topic Node Type

A node type that describes a Kafka topic

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `KafkaTopic` | `radon.nodes.apache.kafka.KafkaTopic` | 1.0.0 | `tosca.nodes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `topic_name` | `true` | `string` |   |   |  The name of the topic. |
| `partitions` | `false` | `integer` |   | 1 | The number of partitions. |
| `replicas` | `false` | `integer` |   | 1 | The number of replicas. |
| `min_insync_replicas` | `false` | `integer` | `greater_or_equal: 0` | 1 | When a producer sets `request_required_acks` to `in_syncs`, this value specifies the minimum number of replicas that must acknowledge a write for the write to be considered successful. |
| `retention` | `false` | `integer` | `greater_or_equal: 1` | 10080 | The number of minutes to keep a log file before deleting it. |
| `roll_time` | `false` | `integer` | `greater_or_equal: 1` | 10080 | Controls the period of time (in minutes) after which Kafka will force the log to roll even if the segment file isn't full to ensure that retention can delete or compact old data. |
| `segment_size` | `false` | `integer` | `greater_or_equal: 1` | 1000000 | Log segment file size in KiB.|

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `broker_urls` | `list` of `string` |   | Represents a list of one or more urls that corresponds to the brokers of the kafka cluster this topic is hosted on. |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
|`kafka_topic` | `radon.capabilities.kafka.KafkaTopic` |   | [0, UNBOUNDED] |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `radon.capabilities.kafka.KafkaHosting` |   | `tosca.relationships.HostedOn` | [1, 1] |
| `openwhisk_invoker` | `radon.capabilities.Invocable` | `radon.nodes.apache.openwhisk.OpenWhiskFunction` | `radon.relationships.apache.openwhisk.KafkaTriggers` | [0, UNBOUNDED] |
| `openfaas_invoker` | `radon.capabilities.Invocable` | `radon.nodes.openfaas.OpenFaaSFunction` | `radon.relationships.openfaas.KafkaTriggers` | [0, UNBOUNDED] |

### Notes
* The `openwhisk_invoker` requirement is optional, and it allows to establish a "Triggers" relationship between the Kafka topic and an OpenWhisk function.
* The `openfaas_invoker` requirement is optional, and it allows to establish a "Triggers" relationship between the Kafka topic and an OpenFaaS function.
* Inputs added to the operations of the `Standard` interface:
  * `create`: `TOPIC_NAME`, `PARTITIONS`, `REPLICAS`, `MIN_INSYNC_REPLICAS`, `RETENTION`, `SEGMENT_SIZE`, `ROLL_TIME` 
