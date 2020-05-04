## Test Policy

This (abstract) policy type represents a test case.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Test` | `radon.policies.testing.Test` | 1.0.0 | |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `ti_blueprint` | `true` | `string` |   |   | Reference to a RADON test infrastructure blueprint |
| `test_id` | `false` | `string` |   |   | Identifier for this test case |

