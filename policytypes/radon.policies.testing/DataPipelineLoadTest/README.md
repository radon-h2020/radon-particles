## Data Pipeline Load Test Policy

This policy type represents a load test case for the Nifi based Data Pipelines.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `DataPipelineLoadTest` | `radon.policies.testing.DataPipelineLoadTest` | 1.0.0 | `radon.policies.testing.LoadTest` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `resources` | `true` | `string` |  |  | A single ZIP archive containing all resources for the test. | 


