## Kafka Broker

This node type represents a Kafka broker that can be scaled outinto a Kafka cluseter.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `KafkaBroker` | `radon.nodes.kafka.KafkaBroker` | 1.0.0 | `radon.nodes.java.JavaApplication` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
|`component_version`| `true`| `version` | `valid_values: [0.10.2.2, 0.11.0.3]` | 0.10.2.2 | The version of the Kafka broker software |
|`scala_version`| `true`| `version`| `valid_values: [2.11, 2.12]` | 2.11 | The Scala verion to be used. |
|`kf_heap_size`| `true` | `scalar-unit.size`| N/A | 1 GiB | This property allows to set the heap memory size that is allocated to Kafka java process.|
|`zk_heap_size`| `true`| `scalar-unit.size`| N/A | 500 MiB | This property allows to set the heap memory size that is allocated to Zookeeper java process.|
|`log_cleaner_enable` | `true`| `boolean`| N/A | `false` | This property allows to enable the default Kafka log cleaner.|

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `java_home` | `string`| `get_attribute: [ HOST, java_home ]` | The path to the Java home at the hosting `JavaRuntime`node. |
| `kafka_home`| `string`| `get_operation_output: [ SELF, Standard, create, KAFKA_HOME ]` | The path to the Kafka home directory. |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
|`host`| `radon.capabilities.kafka.KafkaHosting` | `radon.nodes.kafka.KafkaTopic` | [0, UNBOUNDED] |

### Notes

* Inputs added to the operations of the `Standard` interface:
  * `create`: `KAFKA_VERSION`, `SCALA_VERSION`
  * `configure`: `IP_ADDRESS`, `LOG_CLEANER_ENABLE`, `JAVA_HOME`, `KAFKA_HOME`, `KF_HEAP_SIZE`, `ZK_HEAP_SIZE`
  * `start`:  `JAVA_HOME`, `KAFKA_HOME`
  * `stop`: `JAVA_HOME`, `KAFKA_HOME`
---