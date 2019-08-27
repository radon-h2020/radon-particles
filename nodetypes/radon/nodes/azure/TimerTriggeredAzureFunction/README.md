## Timer-triggered Azure Function Node Type

A node type that represents an Azure function that is triggered by a timer.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `TimerTriggeredAzureFunction` | `radon.nodes.azure.TimerTriggeredAzureFunction` | 1.0.0 | `radon.nodes.azure.AzureFunction` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `schedule` | `true` | `string` |   |   | CRON expression or timespan to describe when and at which frequency the function will be triggered. |

### Notes

* Parameters added to the inputs of operations of the `Standard` interface:
    * `create`: `SCHEDULE` 
