## Precedence Data Type

Data type representing a precedence between two sets of activities.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| Precedence | `radon.datatypes.Precedence` | 1.0.0 | `tosca.datatypes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `type` | `true` | `string` | `valid_values: [sequence, and-fork, and-join, or-fork, or-join, loop]` | sequence | Precedence type |
| `pre_activities` | `true` | `list: string` |   |   | List of pre-activities |
| `post_activities` | `true` | `list: string` |   |   | List of post-activities |
| `parameters` | `false` | `list: float` | `greater_or_equal: 0.0` |   | List of parameters |
