## Response Time Percentile

Policy type representing the expected response time percentile of a TOSCA entity.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `ResponseTimePercentile` | `radon.policies.performance.ResponseTimePercentile` | 1.0.0 | `tosca.policies.Performance` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `rank` | `true` | `integer` | `in_range: [ 1, 100 ]` | N/A |  |
| `lower_bound` | `false` | `float` | `greater_or_equal: 0.0` | N/A | Time in seconds |
| `upper_bound` | `false` | `float` | `greater_or_equal: 0.0` | N/A | Time in seconds |
| `target_entry` | `true` | `string` | N/A | N/A |  |
| `include_phase2` | `false` | `boolean` | N/A | N/A |  |

---