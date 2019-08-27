## NodeJS Application Node Type

The type of a node that represents a Node.js application, and that installs Node.js runtime if necessary.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `radon.nodes.nodejs.NodeJSApplication` | `radon.nodes.nodejs.NodeJSApplication` | 1.0.0 | `tosca.nodes.SoftwareComponent` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `node_version` | `true` | `version` |   | 10.16.0 | The version of the NodeJS runtime this application uses. |

### Notes

* Inputs added to the `Standard` interface operations:
    * `create`: `NODE_VERSION`
