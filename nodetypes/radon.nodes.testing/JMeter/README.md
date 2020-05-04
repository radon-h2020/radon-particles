## Apache JMeter CTT Agent Node Type

This node type represents an agent that can execute load tests with the Apache JMeter tool.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `JMeter` | `radon.nodes.testing.JMeter` | 1.0.0 | `radon.nodes.testing.LoadTestAgent` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `jmeter_properties` | `false` | `string` |   |   | Location and filename of a file with JMeter properties (optional) |
| `worker_hostnames` | `false` | `string` |   |   | Comma-separated list of worker hostnames |

