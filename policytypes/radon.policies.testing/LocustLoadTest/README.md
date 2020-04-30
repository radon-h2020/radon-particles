## Locust Load Test Policy

This policy type represents a load test case for the Apache JMeter tool.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `LocustLoadTest` | `radon.policies.testing.LocustLoadTest` | 1.0.0 | `radon.policies.testing.LoadTest` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `locust_file` | `true` | `string` |   |   | Location and filename of the Locust script |
| `locust_conf` | `false` | `string` |   |   | Location and filename of a file with properties (optional) |


