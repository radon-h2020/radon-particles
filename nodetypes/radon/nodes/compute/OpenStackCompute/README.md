## OpenStack Compute

A type representing a virtual machine on OpenStack.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `VM` | `radon.nodes.openstack.VM` | 1.0.0 | `tosca.nodes.Compute` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description | 
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name`  | `true`  | `string` | N/A | N/A | Name that should be given to the VM in OpenStack |
| `image_id` | `true` | `string` | N/A | N/A | OpenStack image ID (image names are not accepted) |
| `flavor_id` | `true` | `string` | N/A | N/A | OpenStack flavor ID (flavor names are not accepted) |
| `network_id` | `true` | `string` | N/A | N/A | OpenStack network ID (network names are not accepted) |
| `key_name` | `true` | `string` | N/A | N/A | OpenStack SSH key name that should be placed on the VM |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `id` | `string` | N/A | OpenStack ID of the VM |

### Notes

* Inputs added to the `Standard` interface operations:
    * `create`: `NAME`, `IMAGE`, `FLAVOR`, `NETWORK`, `KEY_NAME`
    * `delete`: `ID`

---