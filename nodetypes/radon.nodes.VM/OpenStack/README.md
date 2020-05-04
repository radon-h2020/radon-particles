## OpenStack Compute Node Type

A type representing a virtual machine on OpenStack.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `OpenStack` | `radon.nodes.VM.OpenStack` | 1.0.0 | `tosca.nodes.Compute` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description | 
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name`  | `true`  | `string` |   |   | Name that should be given to the VM in OpenStack |
| `image_id` | `true` | `string` |   |   | OpenStack image ID (image names are not accepted) |
| `flavor_id` | `true` | `string` |   |   | OpenStack flavor ID (flavor names are not accepted) |
| `network_id` | `true` | `string` |   |   | OpenStack network ID (network names are not accepted) |
| `key_name` | `true` | `string` |   |   | OpenStack SSH key name that should be placed on the VM |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `id` | `string` |   | OpenStack ID of the VM |
| `public_address` | `string` |   | OpenStack public IP address of the VM |

### Notes

* Inputs added to the `Standard` interface operations:
    * `create`: `NAME`, `IMAGE`, `FLAVOR`, `NETWORK`, `KEY_NAME`
    * `delete`: `ID`
