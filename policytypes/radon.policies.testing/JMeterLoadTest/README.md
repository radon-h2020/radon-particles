## JMeter Load Test Policy

This policy type represents a load test case for the Apache JMeter tool.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `JMeterLoadTest` | `radon.policies.testing.JMeterLoadTest` | 1.0.0 | `radon.policies.testing.LoadTest` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `jmx_file` | `true` | `string` |   |   | Location and filename of the JMeter test plan |
| `user.properties` | `false` | `string` |   |   | Location and filename of a file with properties for the test plan (optional) |

