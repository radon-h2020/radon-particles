## Load Test Policy

This (abstract) policy type represents a load test case.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `LoadTest` | `radon.policies.testing.Test` | 1.0.0 | `radon.policies.testing.Test` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `hostname` | `false` | `string` |   |   | Convenience property to specify a hostname as the target of the load test (optional) |
| `port` | `false` | `string` |   |   | Convenience property to specify a port as the target of the load test (optional) |

