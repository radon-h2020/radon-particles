## Java Runtime

A type that describes a node capable of installing JRE/JDK and hosting Java applications.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Java` | `radon.nodes.java.Java` | 1.0.0 | `tosca.nodes.SoftwareComponent` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `java_home` | `string` | N/A | The location where JAVA binaries are located |
| `component_version` | `version` | N/A | The version of the Java language (value taken from the `host` capability). |
| `only_jre` | `boolean` | N/A | Indicates whether only the JRE is required (value taken from the `host` capability).|
| `headless` | `boolean`  | N/A | Specifies whether headless mode is enough as the components are run on a server and do not need equipment such as display or keyboard (value taken from the `host` capability). |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `radon.capabilities.container.JavaRuntime` | `tosca.nodes.Container.Application` | [0, UNBOUNDED] |

### Notes

* Inputs added to the `Standard` interface operations:
    * `create`: `JAVA_VERSION`, `JAVA_IS_JRE`, `JAVA_IS_HEADLESS`
    * `delete`: `JAVA_VERSION`, `JAVA_HOME`

---