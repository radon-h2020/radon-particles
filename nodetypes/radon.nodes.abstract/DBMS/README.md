![](https://img.shields.io/badge/Status:-RELEASED-green)

## DBMS Node Type (Abstract)

Abstract node type representing a DBMS.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `DBMS` | `radon.nodes.abstract.DBMS` | 1.0.0 | `tosca.nodes.DBMS` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `false` | `string` |   |   | Name of the DBMS |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `tosca.capabilities.Compute` | `[radon.nodes.abstract.Database]` | [1, UNBOUNDED] |
