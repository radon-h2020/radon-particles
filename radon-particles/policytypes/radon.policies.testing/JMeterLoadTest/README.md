## JMeter Load Test Policy

This policy type represents a load test case for the Apache JMeter tool.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `JMeterLoadTest` | `radon.policies.testing.JMeterLoadTest` | 1.0.0 | `radon.policies.testing.LoadTest` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `jmx_file_name` | `true` | `string` |   | `testplan.jmx` | The name of the test plan file (.jmx) inside the resources ZIP archive. If resources is a .jmx file itself, this property is ignored (default: testplan.jmx) |
| `resources` | `true` | `string` |  |  | Either a single test plan file (.jmx) or a ZIP archive containing all resources for the test. | 
| `user.properties` | `false` | `string` |   |   | Location and filename of a file with properties for the test plan (optional) |

