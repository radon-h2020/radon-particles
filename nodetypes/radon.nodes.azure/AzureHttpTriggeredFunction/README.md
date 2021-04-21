![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Azure HTTP-Triggered Function Node Type

A node type that represents an Azure function which is triggered by an HTTP call.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureHttpTriggeredFunction` | `radon.nodes.azure.AzureHttpTriggeredFunction` | 1.0.0 | `radon.nodes.azure.AzureFunction` |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `url` | `string` | `get_operatoin_output: [SELF, Standard, create, URL]` | The URL at which the function can be invoked |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `auth_level` | `false` | `string` | `valid_values: [anonymous, function, admin]` |   | Determines what keys, if any, need to be present on the request in order to invoke the function |
| `methods` | `false` | `list` of `string` |   |   | An array of the HTTP methods to which the function responds. If not specified, the function responds to all HTTP methods |
| `route` | `false` | `string` |   |   | Defines the route template, controlling to which request URLs your function responds. The default value, if none is provided, is the function name |
| `route_prefix` | `true` | `string` |   |  "api" | The route prefix that applies to all routes. Use an empty string to remove the default prefix |
| `max_outstanding_requests` | `true` | `integer` |   | 200 | The maximum number of outstanding requests that are held at any given time |
| `max_concurrent_requests` | `true` | `integer` |   | 100 | The maximum number of http functions that will be executed in parallel |

### Notes

* Parameters added to the inputs of the operations of the `Standard` interface:
    * `create`: `AUHT_LEVEL`, `METHODS`, `ROUTE`, `MAX_OUTSTANDING_REQUESTS`, `MAX_CONCURRENT_REQUESTS`
* An output parameter with the name `URL` is expected from the `create` operation of the `Standard` interface.
