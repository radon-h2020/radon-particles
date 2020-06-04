## Triggers Relationship (Abstract)

Abstract relationship type representing triggering of an invocable node.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Triggers` | `radon.relationships.abstract.Triggers` | 1.0.0 | `tosca.relationships.Root` |

### Valid Target types

* `radon.capabilities.Invocable`

### Properties

| Name | Required | Type | Constraint | Default Value| Description |
|:---- |:-------- |:---- |:---------- |:-----------  |:----------- |
| `events` | `true` | `list: radon.datatypes.Event` |   |   | List of events |
| `interactions` | `false` | `list: radon.datatypes.Interaction` |   |   | List of interactions |
