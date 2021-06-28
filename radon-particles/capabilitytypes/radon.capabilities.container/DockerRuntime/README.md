## Docker Runtime Capability

The type indicates capabilities of a Docker runtime environment. 

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `DockerRuntime` | `radon.capabilities.container.DockerRuntime` | 1.0.0 | `tosca.capabilities.Container` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |  
| `version` | `false` | `version` |   |   | The supported Docker version |
| `publish_ports` | `false` | `list` of `PortSpec` |   | List of ports mappings from source (Docker container) to target (host) ports to publish |
| `expose_ports` | `fasle` | `list` of `PortSpec` |   | List of ports mappings from source (Docker container) to expose to other Docker containers (not accessible outside host) |   
| `volumes` | `false` | `list` of `string` | |  List of volume mappings to enable access from the Docker container to a directory on the host machine |
| `port` | `true` | `integer` |   | 2375 | Port number of the exposed Docker API | 

### Notes

* When the expose_ports property is used, only the source and source_range properties of PortSpec would be valid for supplying port numbers or ranges, the target and target_range properties would be ignored.
