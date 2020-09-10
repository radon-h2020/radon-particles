![](https://img.shields.io/badge/Status:-RELEASED-green)

## Google Cloud Resource Node Type

An abstract node type to describe a generic Google Cloud Resource. All specific Google Cloud Resources should derive from this type.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `GoogleCloudResource` | `radon.nodes.google.GoogleCloudResource` | 1.0.0 | `tosca.nodes.SoftwareComponent` |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.google.GoogleCloudPlatform` | `HostedOn` | [1, 1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.google.CloudFunctioN` | `radon.relationships.google.Triggers` | [0, UNBOUNDED] |
