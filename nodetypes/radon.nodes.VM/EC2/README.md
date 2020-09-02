![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AWS EC2 Compute Node Type

A type representing an EC2 virtual machine on AWS.


| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `EC2` | `radon.nodes.VM.EC2` | 1.0.0 | `tosca.nodes.Compute` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `image`  | `true`  | `string` |   | ami-00890f614e48ce866 | EC2 image ID |
| `instance_type` | `true` | `string` |  | t2.micro | EC2 instance type ID |
| `ssh_key_name` | `true` | `string` |  |  | Name of the SSH key name to be used |
| `ssh_key_file` | `true` | `string` |  |  | Path to the SSH key file on the filesystem (required by the orchestrator) |
| `ssh_user` | `true` | `string` |  |  | User to be used for SSH access |
| `vpc_subnet_id` | `true` | `string` |  |  | AWS VPC subnet id where the VM should be created in |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `id` | `string` |   | EC2 ID of the VM |
