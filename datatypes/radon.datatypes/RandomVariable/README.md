## Random Variable Data Type

Data type representing a random variable that always takes non-negative values.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| RandomVariable | `radon.datatypes.RandomVariable` | 1.0.0 | `tosca.datatypes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `mean` | `true` | `float` | `greater_or_equal: 0.0` | 1.0 | Mean value |
| `scv` | `false` | `float` | `greater_or_equal: 0.0` |   | Squared coefficient of variation |
