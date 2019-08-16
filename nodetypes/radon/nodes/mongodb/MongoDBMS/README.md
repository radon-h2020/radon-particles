## MongoDB DBMS Node Type

A node type that describes a MongoDB DBMS.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `MongoDBMS` | `radon.nodes.mongodb.MongoDBMS` | 1.0.0 | `tosca.nodes.DBMS` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `component_version` | `true` | `version` | `valid_values: [3.2,3.4,3.6]` | 3.6 | The version of the MongoDB DBMS |
| `port` | `true` | `integer` | `equal: 27017` | 27017 | The listening port of the DBMS |
| `db_path` | `true` | `string` | N/A |  `/var/lib/mongo` | The path where database files will be stored |
| `authorization_enabled` | `true` | `boolean` | N/A | `false` | Identifies whether users should be authenticated |
| `administrator` | `false` | `string` | N/A | N/A | The username of the administrator |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:---------- |:------------- |
| `url` | `string` | `concat: ["http://", get_attribute: [HOST, public_address], get_property: [SELF, port] ]` | The URL used to formulate the connection string |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `tosca.capabilities.Compute` | `radon.nodes.mongodb.MongoDBDatabase` | [1, UNBOUNDED]|

### Notes

* Inputs added to the `Standard` interface operations:
  * `create`: `IP_ADDRESS`, `MONGODB_VERSION`, `MONGODB_PORT`, `MONGODB_DB_PATH`, `MONGODB_AUTHORIZATION`, `MONGODB_ADMIN`, `MONGODB_ROOT_PASSWORD`
