![](https://img.shields.io/badge/Status:-RELEASED-green)

## Object Storage Node Type (Abstract)

Abstract node type representing an object storage independently of the underlying provider.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `ObjectStorage` | `radon.nodes.abstract.ObjectStorage` | 1.0.0 | `tosca.nodes.Storage.ObjectStorage` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `entries`<sup>[1](#fn1)</sup> | `false` | `map: radon.datatypes.Entry` |   |   | Map of entries |
<sup name="fn1">1</sup> The name of each `Entry` must be prefixed with the name of the operation that it is associated with, e.g. "get", "get_image" and and "getImage". This enables the decomposition tool to compute the operating cost of the `ObjectStorage`. The supported operations currently include GET, PUT and DELETE.

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.abstract.CloudPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.abstract.Function` | `radon.relationships.Triggers` | [0, UNBOUNDED] |
