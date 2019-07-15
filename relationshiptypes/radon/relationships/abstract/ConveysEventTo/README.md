## Display Name

This is an abstract Relationship Type that represents a binding between an event source, e.g., an object store, and an event target, e.g., a FaaS function.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| ConveysEventTo | radon.relationships.abstract.ConveysEventTo | 1.0.0 | tosca.relationships.Root |

### Properties

| Name | Required | Type | Constraint | Description |
|:---- |:-------- |:---- |:---------- |:----------- |
| `events` | `false` | `list` | N/A | A list of events of type `radon.datatypes.Event` that are conveyed to the target |


### Attributes

| Name | Required | Type | Constraint | Description |
|:---- |:-------- |:---- |:---------- |:----------- |

### Capabilities

| Name | Type | Valid Source Types |
|:---- |:---- |:------------------ |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|

### Notes

* Arbitrary list of additional notes
* ...

---
