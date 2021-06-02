![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Mongo Database Node Type

A node type that describes a Mongo database.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `MongoDatabase` | `radon.nodes.mongodb.MongoDatabase` | 1.0.0 | `radon.nodes.abstract.Database` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `user` | `true` | `string` |   |   | The user name for the database |
| `password` | `true` | `string` |   |   | The user password for the database |
| `authentication_database` | `false` | `string` |   |   | If authorization is enabled by the host, defines the database where the user authentication data is stored |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Compute` | `radon.nodes.mongodb.MongoDBMS` | `tosca.relationships.HostedOn` | [1, 1] |

### Notes

* If authorization is enabled by the host, the properties: `user`, `password`, and `authentication_database` must be assigned values.
* Inputs added to the `Standard` interface:
    * `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_USER_AUTH_DB`
