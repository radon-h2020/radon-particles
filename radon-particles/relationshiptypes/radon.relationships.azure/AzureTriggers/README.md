## Azure Triggers Relationship

Azure-specific relationship type representing AzureResource-to-AzureFunction communication.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureTriggers` | `radon.relationships.azure.AzureTriggers` | 1.0.0 | `radon.relationships.Triggers` |

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
