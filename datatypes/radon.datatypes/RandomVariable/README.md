## Random Variable Data Type

Data type representing a random variable that always takes non-negative values.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| RandomVariable | `radon.datatypes.RandomVariable` | 1.0.0 | `tosca.datatypes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `mean`<sup>[1](#fn1)</sup> | `true` | `float` | `greater_or_equal: 0.0` | 1.0 | Mean value |
| `scv`<sup>[1](#fn1)</sup> | `false` | `float` | `greater_or_equal: 0.0` |   | Squared coefficient of variation |

<sup>[1](#fn1)</sup> The `scv` is only reserved for now due to the limitation of the underlying LQN solver invoked by the decomposition tool. Notably, a zero `mean` implies a zero `scv` and therefore should also be avoided. A workaround for this is to replace zero with a small value like 0.001.
