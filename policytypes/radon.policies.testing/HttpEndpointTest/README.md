## HTTP Endpoint Test Policy

Policy type representing a test case specification for a HTTP endpoint test.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `HttpEndpointTest` | `radon.policies.testing.HttpEndpointTest` | 1.0.0 | `radon.policies.testing.Test` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `use_https` | `true` | `boolean` |   | `true` | If https shall be used |
| `method` | `true` | `string` |   | GET | The http method to use |
| `hostname` | `true` | `string` |   |   | The host to use |
| `port` | `true` | `integer` |   | 80 | The port to use |
| `path` | `true` | `string` |   |   | The path to use |
| `test_body` | `false` | `json` |   |   | The body to use as json |
| `test_header` | `false` | `map of string` |   |   | The http headers to use |
| `expected_status` | `true` | `integer` |   | 200 | The expected http status return code |
| `expected_body` | `false` | `json` |   |   | The expected body value as json |
