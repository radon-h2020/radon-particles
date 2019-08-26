## Response Time Percentile Policy

Policy type representing the expected response time percentile of a TOSCA entity.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `ResponseTimePercentile` | `radon.policies.performance.ResponseTimePercentile` | 1.0.0 | `tosca.policies.Performance` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `rank` | `true` | `integer` | `in_range: [ 1, 100 ]` |   |  |
| `lower_bound` | `false` | `float` | `greater_or_equal: 0.0` |   | Time in seconds |
| `upper_bound` | `false` | `float` | `greater_or_equal: 0.0` |   | Time in seconds |
| `target_entry` | `true` | `string` |   |   | The target entry |
| `include_phase2` | `false` | `boolean` |   |   | Whether to be included in phase two or not |
