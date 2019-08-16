## Java Runtime Capability

The type indicates capabilities of a Java runtime environment. 

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `JavaRuntime` | `radon.capabilities.container.JavaRuntime` | 1.0.0 | `tosca.capabilities.Container` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `java_version` | `true` | `integer` | N/A | 8 | The version of the Java language.|
| `only_jre` | `true` | `boolean` | N/A | `true` | Indicates whether only the JRE is required. |
| `headless` | `true` | `boolean`  | N/A | `true` | Specifies whether headless mode is enough as the components are run on a server and do not need equipment such as display or keyboard. |

### Valid Source Types

* `radon.nodes.java.JavaApplication`
