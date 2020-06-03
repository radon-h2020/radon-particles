## Mean Response Time Policy

Policy type representing the required mean response time of a request.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `MeanResponseTime` | `radon.policies.performance.MeanResponseTime` | 1.0.0 | `tosca.policies.Performance` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `target_entries` | `false` | `list: string` |   |   | List of target entries |
| `lower_bound` | `false` | `float` | `greater_or_equal: 0.0` |   | Lower bound in seconds |
| `upper_bound` | `false` | `float` | `greater_or_equal: 0.0` |   | Upper bound in seconds |
