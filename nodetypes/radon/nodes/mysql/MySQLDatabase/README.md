## MySQL Database

Node type to represent the logical database that can be managed and hosted on MySQL.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `MySQLDatabase` | `radon.nodes.mysql.MySQLDatabase` | 1.0.0 | `tosca.nodes.Database` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |  
| `user` | `true` | `string` | N/A | N/A | the required user account name for DB administration |
| `password` | `true` | `string` | N/A | N/A | the required password for the DB user account |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `database_endpoint` | `tosca.capabilities.Endpoint.Database` | N/A | [0, UNBOUNDED] |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Compute` | `radon.nodes.mysql.MySQLDBMS` | `tosca.relationships.HostedOn` | [1,1] |

### Notes

* Inputs added to the `Standard` interface:
    * `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DBMS_ROOT_PASSWORD`

---