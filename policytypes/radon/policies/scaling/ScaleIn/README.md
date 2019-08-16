## Scale In Policy

Policy type representing a scale-in configuration for a TOSCA entity.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `ScaleIn` | `radon.policies.scaling.ScaleIn` | 1.0.0 | `tosca.policies.Scaling` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `cpu_lower_bound` | `false` | `float` | `greater_or_equal: 0.0` | N/A | The lower bound for the CPU |
| `cpu_upper_bound` | `false` | `float` | `less_or_equal: 100.0` | N/A | The upper bound for the CPU |
| `adjustment` | `false` | `integer` | `less_or_equal: -1` | N/A | The amount by which to scale |
