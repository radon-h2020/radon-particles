## Auto Scale

Policy type representing an auto-scaling configuration for a TOSCA entity.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AutoScale` | `radon.policies.scaling.AutoScale` | 1.0.0 | `tosca.policies.Scaling` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `min_size` | `true` | `integer` | `greater_or_equal: 1` | N/A | The minimum number of instances |
| `max_size` | `true` | `integer` | N/A | N/A | The maximum number of instances |

---