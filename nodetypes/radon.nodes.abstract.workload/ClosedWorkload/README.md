![](https://img.shields.io/badge/Status:-RELEASED-green)

## Closed Workload Node Type (Abstract)

Abstract node type representing a closed workload in general.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `ClosedWorkload` | `radon.nodes.abstract.workload.ClosedWorkload` | 1.0.0 | `radon.nodes.abstract.Workload` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `population` | `true` | `integer` | `greater_or_equal: 1` | 1 | Population |
| `think_time` | `true` | `radon.datatypes.RandomVariable` |   |   | Think time |
