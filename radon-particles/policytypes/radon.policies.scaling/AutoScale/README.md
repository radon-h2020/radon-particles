## Auto Scale Policy

Policy type representing an auto-scaling configuration for a TOSCA entity.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AutoScale` | `radon.policies.scaling.AutoScale` | 1.0.0 | `tosca.policies.Scaling` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `min_size` | `true` | `integer` | `greater_or_equal: 1` |   | The minimum number of instances |
| `max_size` | `true` | `integer` |   |   | The maximum number of instances |
