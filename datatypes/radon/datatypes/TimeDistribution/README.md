## Time Distribution Data Type

Data type representing a time distribution.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| TimeDistribution | `radon.datatypes.TimeDistribution` | 1.0.0 | `tosca.datatypes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `mean` | `true` | `integer` | `greater_or_equal: 0` | N/A | The mean value |
| `scv` | `true` | `float` | `greater_or_equal: 0.0` | N/A | The squared coefficient of variation |
