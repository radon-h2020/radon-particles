## Entry Data Type

Data type representing an entry at a TOSCA node.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| Entry | `radon.datatypes.Entry` | 1.0.0 | `tosca.datatypes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `activities` | `true` | `map: radon.datatypes.Activity` |   |   | Map of activities |
| `precedences` | `false` | `list: radon.datatypes.Precedence` |   |   | List of precedences |
