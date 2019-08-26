## Triggers Relationship (Abstract)

This is an abstract Relationship Type that represents a binding between an event source, e.g., an object store, and an event target, e.g., a FaaS function.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Triggers` | `radon.relationships.abstract.Triggers` | 1.0.0 | `tosca.relationships.Root` |

### Valid Target types

* `radon.capabilities.Invocable`

### Properties

| Name | Required | Type | Constraint | Default Value| Description |
|:---- |:-------- |:---- |:---------- |:-----------  |:----------- |
| `events` | `false` | `list` |   |   | A list of events of type `radon.datatypes.Event` that are conveyed to the target |
