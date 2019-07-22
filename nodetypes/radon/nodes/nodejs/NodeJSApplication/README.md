## NodeJS Application

The type of a node that represents a Node.js application, and that installs Node.js runtime if necessary.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `radon.nodes.nodejs.NodeJSApplication` | `radon.nodes.nodejs.NodeJSApplication` | 1.0.0 | `tosca.nodes.SoftwareComponent` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `node_version` | `true` | `version` | N/A | 10.16.0 | The version of the NodeJS runtime this application uses. |

### Notes

* Inputs added to the `Standard` interface operations:
    * `create`: `NODE_VERSION`

---