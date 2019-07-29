## Java Runtime

A type that describes a node capable of installing JRE/JDK and hosting Java applications.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Java` | `radon.nodes.java.Java` | 1.0.0 | `tosca.nodes.SoftwareComponent` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `java_home` | `string` | The `java_home` attribute exposed by the `host` capability | The location where JAVA binaries are located |
| `component_version` | `version` | The `java_version` attribute exposed by the `host` capability | The version of the Java language (value taken from the `host` capability). |
| `only_jre` | `boolean` | The `only_jre` attribute exposed by the `host` capability | Indicates whether only the JRE is required (value taken from the `host` capability).|
| `headless` | `boolean`  | The `headless` attribute exposed by the `host` capability | Specifies whether headless mode is enough as the components are run on a server and do not need equipment such as display or keyboard (value taken from the `host` capability). |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `radon.capabilities.container.JavaRuntime` | `tosca.nodes.Container.Application` | [0, UNBOUNDED] |

### Notes

* Inputs added to the `Standard` interface operations:
    * `create`: `JAVA_VERSION`, `JAVA_IS_JRE`, `JAVA_IS_HEADLESS`
    * `delete`: `JAVA_VERSION`, `JAVA_HOME`

---