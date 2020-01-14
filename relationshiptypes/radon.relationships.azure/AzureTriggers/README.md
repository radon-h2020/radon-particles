## Azure Triggers Relationship

An abstract relationship type representing AzureResource-to-AzureCFunction communication.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureTriggers` | `radon.relationships.azure.AzureTriggers` | 1.0.0 | `radon.relationships.abstract.Triggers` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
|`events`|`true`|`list` of `radon.datatypes.Event`|`length: 1`|   | The event associated with this relationship |

### Notes

* The following parameters are added to tht inputs of the `Configure` interface:
    * `EVENT`: taken from the `events` property
    * `RESOURCE`: the `name` of the `SOURCE` Azure Resource
    * `FUNCTION_NAME`
    * `TIMEOUT`
    * `APP_NAME`
    * `APP_RUNTIME`
    * `APP_OS_TYPE`
    * `APP_STORAGE_ACCOUNT`
    * `APP_RESOURCE_GROUP`
* A template of this type should provide implementation artifacts that deploy the Azure Function specified at the `TARGET` side.
