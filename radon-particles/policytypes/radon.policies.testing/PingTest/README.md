## Ping Test Policy

Policy type representing a test case specification for a ping test.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `PingTest` | `radon.policies.testing.PingTest` | 1.0.0 | `radon.policies.testing.Test` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `hostname` | `true` | `string` |   |   | The hostname to be used as the destination for the ping test |
