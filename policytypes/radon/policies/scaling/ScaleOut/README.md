## Scale Out

Policy type representing a scale-out configuration for a TOSCA entity.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `ScaleOut` | `radon.policies.scaling.ScaleOut` | 1.0.0 | `tosca.policies.Scaling` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `cpu_lower_bound` | `false` | `float` | `greater_or_equal: 0.0` | N/A | The lower bound for the CPU |
| `cpu_upper_bound` | `false` | `float` | `less_or_equal: 100.0` | N/A | The upper bound for the CPU |
| `adjustment` | `false` | `integer` | `greater_or_equal: 1` | N/A | The amount by which to scale |

---