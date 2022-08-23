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

\* The following table summarizes valid settings for the properties of a `Precedence`.

| Type | Pre-Activities | Post-Activities | Parameters:<br>&bull; Number<sup>[1](#fn1)</sup> | <br>&bull; Description |
|:---- |:-------------- |:--------------- |:------------------------------------------------ |:---------------------- |
| `sequence` | single | single | 0 | N/A |
| `and-fork` | single | multiple | 0 | N/A |
| `and-join` | multiple | single | 1 | Number of pre-activities that must be completed before the join |
| `or-fork` | single | multiple | *n* | Probability that each of the *n* post-activities is chosen as the next one to perform |
| `or-join` | multiple | single | 0 | N/A |
| `loop` | single | multiple | *n*-1 | Number of times that each of the first *n*-1 post-activities is repeated |

<sup id="fn1">1</sup> *n* denotes the number of post-activities.
