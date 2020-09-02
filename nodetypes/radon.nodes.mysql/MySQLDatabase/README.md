![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## MySQL Database Node Type

Node type to represent the logical database that can be managed and hosted on MySQL.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `MySQLDatabase` | `radon.nodes.mysql.MySQLDatabase` | 1.0.0 | `tosca.nodes.Database` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `user` | `true` | `string` |   |   | the required user account name for DB administration |
| `password` | `true` | `string` |   |   | the required password for the DB user account |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `database_endpoint` | `tosca.capabilities.Endpoint.Database` |   | [0, UNBOUNDED] |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Compute` | `radon.nodes.mysql.MySQLDBMS` | `tosca.relationships.HostedOn` | [1, 1] |

### Notes

* Inputs added to the `Standard` interface:
    * `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DBMS_ROOT_PASSWORD`
