![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## MySQL Database Node Type

A node type that describes a MySQL database.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `MySQLDatabase` | `radon.nodes.mysql.MySQLDatabase` | 1.0.0 | `radon.nodes.abstract.Database` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `user` | `true` | `string` |   |   | The user name for the database |
| `password` | `true` | `string` |   |   | The user password for the database |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Compute` | `radon.nodes.mysql.MySQLDBMS` | `tosca.relationships.HostedOn` | [1, 1] |

### Notes

* Inputs added to the `Standard` interface:
    * `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DBMS_ROOT_PASSWORD`
