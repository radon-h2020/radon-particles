## Triggers Relationship (Abstract)

Abstract relationship type representing connection to an endpoint node.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `ConnectsTo` | `radon.relationships.abstract.ConnectsTo` | 1.0.0 | `tosca.relationships.ConnectsTo` |

### Properties

| Name | Required | Type | Constraint | Default Value| Description |
|:---- |:-------- |:---- |:---------- |:-----------  |:----------- |
| `interactions` | `false` | `list: radon.datatypes.Interaction` |   |   | List of interactions |
