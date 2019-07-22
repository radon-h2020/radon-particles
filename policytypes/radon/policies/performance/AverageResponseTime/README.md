## Average Response Time

Policy type representing the expected average response time of a TOSCA entity.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AverageResponseTime` | `radon.policies.performance.AverageResponseTime` | 1.0.0 | `tosca.policies.Performance` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `lower_bound` | `false` | `float` | `greater_or_equal: 0.0` | N/A | Time in seconds |
| `upper_bound` | `false` | `float` | `greater_or_equal: 0.0` | N/A | Time in seconds |
| `target_entry` | `true` | `string` | N/A | N/A |  |
| `include_phase2` | `false` | `boolean` | N/A | N/A |  |

---