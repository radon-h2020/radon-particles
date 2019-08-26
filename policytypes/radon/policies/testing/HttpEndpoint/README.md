## HTTP Endpoint Test Policy

Policy type representing a test case specification for a HTTP endpoint test.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `HttpEndpoint` | `radon.policies.testing.HttpEndpoint` | 1.0.0 | `radon.policies.testing.TestCase` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `use_https` | `true` | `boolean` | N/A | `true` | If https shall be used |
| `method` | `true` | `string` | N/A | GET | The http method to use |
| `hostname` | `true` | `string` | N/A | N/A | The host to use |
| `port` | `true` | `integer` | N/A | 80 | The port to use |
| `path` | `true` | `string` | N/A | N/A | The path to use |
| `test_body` | `false` | `json` | N/A | N/A | The body to use as json |
| `test_header` | `false` | `map of string` | N/A | N/A | The http headers to use |
| `expected_status` | `true` | `integer` | N/A | 200 | The expected http status return code |
| `expected_body` | `false` | `json` | N/A | N/A | The expected body value as json |
