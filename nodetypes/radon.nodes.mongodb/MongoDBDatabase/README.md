## MongoDB Database Node Type

A node type that describes a MongoDB database.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `MongoDBDatabase` | `radon.nodes.mysql.MongoDBDatabase` | 1.0.0 | `tosca.nodes.Database` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `authentication_database` | `false` | `string` |   |   | If authorization is enabled by the host, defines the database where the user authentication data is stored |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `database_endpoint` | `tosca.capabilities.Endpoint.Database` |   | [0, UNBOUNDED] |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Compute` | `radon.nodes.mongodb.MongoDBMS` | `tosca.relationships.HostedOn` | [1, 1] |

### Notes

* If authorization is enabled by the host, the properties: `user`, `password`, and `authentication_database` must be assigned values.    
* Inputs added to the `Standard` interface:
    * `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_USER_AUTH_DB`
