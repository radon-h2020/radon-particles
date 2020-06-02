## Entries Data Type

Data type representing the set of entries at an object storage.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| Entries | `radon.datatypes.objectstorage.Entries` | 1.0.0 | `tosca.datatypes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `get` | `false` | `radon.datatypes.Entry` |   |   | Get entry |
| `put` | `false` | `radon.datatypes.Entry` |   |   | Put entry |
| `delete` | `false` | `radon.datatypes.Entry` |   |   | Delete entry |
