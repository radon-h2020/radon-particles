## Performance Policy

Abstract policy type representing a performance requirement.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Performance` | `radon.policies.Performance` | 1.0.0 | `tosca.policies.Performance` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `target_entries` | `false` | `list: string` |   |   | List of target entries |
| `lower_bound` | `false` | `float` | `greater_or_equal: 0.0` |   | Lower bound |
| `upper_bound` | `false` | `float` | `greater_or_equal: 0.0` |   | Upper bound |
