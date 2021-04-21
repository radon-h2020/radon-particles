![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## Prometheus Pushgateway Node Type

A type representing prometheus gateway instance deployed on a VM.

| Name          | URI                                  | Version | Derived From                           |
| :------------ | :----------------------------------- | :------ | :------------------------------------- |
| `PushGateway` | `radon.nodes.monitoring.PushGateway` | 1.0.0   | `radon.nodes.docker.DockerApplication` |

### Properties

| Name                       | Required | Type     | Constraint | Default Value | Description                       |
| :------------------------- | :------- | :------- | :--------- | :------------ | :-------------------------------- |
| `user_email`               | `true`   | `string` |            |               | Account to set Graphana dashboard |
| `consul_ip`                | `true`   | `string` |            |               | Consul Service IP                 |
| `pushgateway_service_port` | `true`   | `string` |            |               | Port that exposes pushgateway     |
| `grafana_api_ip`           | `true`   | `string` |            |               | Grafana ip                        |

### Attributes

| Name             | Required | Type     | Constraint | Default Value | Description                     |
| :--------------- | :------- | :------- | :--------- | :------------ | :------------------------------ |
| `pushgateway_ip` | `true`   | `string` |            |               | Prometheus Pushgateway instance |

### Artifacts

| Name        | Description                         |
| :---------- | :---------------------------------- |
| `create`    | deploy prometheus pushgateway       |
| `configure` | Inject in Consul and set up Grafana |
| `delete`    | Remove the entry from Consul        |
