![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Azure Timer-Triggered Function Node Type

A node type that represents an Azure function which is triggered by a predefined timer.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureTimerTriggeredFunction` | `radon.nodes.azure.AzureTimerTriggeredFunction` | 1.0.0 | `radon.nodes.azure.AzureFunction` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `schedule` | `true` | `string` |   |   | A CRON expression or timespan to describe when and at which frequency the function will be triggered |

### Notes

* Parameters added to the inputs of operations of the `Standard` interface:
    * `create`: `SCHEDULE`
