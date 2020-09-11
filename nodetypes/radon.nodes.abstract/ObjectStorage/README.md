![](https://img.shields.io/badge/Status:-RELEASED-green)

## Object Storage Node Type (Abstract)

Abstract node type representing an object storage independently of the underlying provider.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `ObjectStorage` | `radon.nodes.abstract.ObjectStorage` | 1.0.0 | `tosca.nodes.Storage.ObjectStorage` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `entries` | `false` | `map: radon.datatypes.Entry` |   |   | Map of entries<sup>[1](#fn1)</sup> |
<sup name="fn1">1</sup> Entry names must be prefixed with an operation, e.g. `get` and `get_image`. The supported operations include `get`, `put` and `delete`.

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.abstract.CloudPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.abstract.Function` | `radon.relationships.abstract.Triggers` | [0, UNBOUNDED] |
