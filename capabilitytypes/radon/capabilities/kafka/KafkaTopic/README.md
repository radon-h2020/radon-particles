## Kafka Topic

This capability type describes a node that represents a Kafka Topic

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `KafkaTopic` | `radon.capabilities.kafka.KafkaTopic` | 1.0.0 | `tosca.capabilities.Root` |

### Notes
* A node template that uses this capability should provide values for the the `ip_address` and `port` properties so that topic consumers can establish connection to the suitable Kafka bootstrap server.

---