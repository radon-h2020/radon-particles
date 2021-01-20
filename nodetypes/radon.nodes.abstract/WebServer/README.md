![](https://img.shields.io/badge/Status:-RELEASED-green)

## Web Server Node Type (Abstract)

Abstract node type representing a web server.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `WebServer` | `radon.nodes.abstract.WebServer` | 1.0.0 | `tosca.nodes.WebServer` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `false` | `string` |   |   | Name of the web server |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `tosca.capabilities.Compute` | `[radon.nodes.abstract.WebApplication]` | [1, UNBOUNDED] |
