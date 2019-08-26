## TCP Ping Test Policy

Policy type representing a test case specification for a TCP ping test.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `TcpPing` | `radon.policies.testing.TcpPing` | 1.0.0 | `radon.policies.testing.TestCase` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `port` | `true` | `integer` |   |   | The port to ping during the test |
