## Kafka Topic

A node type that describes a Kafka topic

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `KafkaTopic` | `radon.nodes.kafka.KafkaTopic` | 1.0.0 | `tosca.nodes.Root` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `topic_name` | `true` | `string` | `pattern: "[-_A-Za-z0-9]+"` | N/A |  The name of the topic. |
| `partitions` | `false` | `integer` | N/A | 1 | The number of partitions. |
| `replicas` | `false` | `integer` | N/A | 1 | The number of replicas. |
| `min_insync_replicas` | `false` | `greater_or_equal: 0` | 1 | When a producer sets `request_required_acks` to `in_syncs`, this value specifies the minimum number of replicas that must acknowledge a write for the write to be considered successful. |
| `retention` | `false` | `scalar-unit.time` | `greater_or_equal: 1 m` | 7 d | The number of minutes to keep a log file before deleting it. |
| `roll_time` | `false` | `scalar-unit.time` | `greater_or_equal: 1 m` | 7 d | Controls the period of time after which Kafka will force the log to roll even if the segment file isn't full to ensure that retention can delete or compact old data. |
| `segment_size` | `false` | `scalar-unit.size` | `greater_or_equal: 1 KiB` | 1 GiB | Log segment file size.|

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
|`kafka_topic` | `radon.capabilities.kafka.KafkaTopic` | N/A | [0, UNBOUNDED] |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `radon.capabilities.kafka.KafkaHosting` | N/A | `tosca.relationships.HostedOn` | [1,1] |

### Notes

* Inputs added to the operations of the `Standard` interface:
  * `create`: `TOPIC_NAME`, `PARTITIONS`, `REPLICAS`, `MIN_INSYNC_REPLICAS`, `RETENTION`, `SEGMENT_SIZE`, `ROLL_TIME` 

---