## MySQL DBMS

A MySQL database management system.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `MySQLDBMS` | `radon.nodes.mysql.MySQLDBMS` | 1.0.0 | `tosca.nodes.DBMS` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description | 
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `root_password`  | `true`  | `string` | N/A | N/A | The root password of the DBMS  |
| `port` | `false` | `integer` | N/A | 3306 | The listening port of the DBMS |
| `component_version` | `true` | `version` | N/A | 5.6 | The version of the MySQL DBMS |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
|`host`| `tosca.capabilities.Compute`| `radon.nodes.mysql.MySQLDatabase` | [1, UNBOUNDED] |

### Notes

* Inputs added to the `Standard` interface operations:
    * `configure`: `DBMS_ROOT_PASSWORD`, `DBMS_PORT`

---