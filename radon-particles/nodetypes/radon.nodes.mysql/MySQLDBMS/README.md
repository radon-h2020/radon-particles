![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## MySQL DBMS Node Type

A node type that describes a MySQL DBMS.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `MySQLDBMS` | `radon.nodes.mysql.MySQLDBMS` | 1.0.0 | `radon.nodes.abstract.DBMS` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `component_version` | `true` | `version` |   | 5.6 | The version of the DBMS |
| `root_password` | `true` | `string` |   |   | The root password of the DBMS |
| `port` | `false` | `integer` |   | 3306 | The listening port of the DBMS |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `tosca.capabilities.Compute` | `radon.nodes.mysql.MySQLDatabase` | [1, UNBOUNDED] |

### Notes

* Inputs added to the `Standard` interface operations:
    * `configure`: `DBMS_VERSION`, `DBMS_ROOT_PASSWORD`, `DBMS_PORT`
