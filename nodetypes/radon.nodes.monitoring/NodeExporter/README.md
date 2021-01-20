![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## Node Exporter Node Type

A type representing a node exporter instance deployed on a VM.

| Name           | URI                                   | Version | Derived From                           |
| :------------- | :------------------------------------ | :------ | :------------------------------------- |
| `NodeExporter` | `radon.nodes.monitoring.NodeExporter` | 1.0.0   | `radon.nodes.docker.DockerApplication` |

### Properties

| Name                         | Required | Type     | Constraint | Default Value | Description        |
| :--------------------------- | :------- | :------- | :--------- | :------------ | :----------------- |
| `node_exporter_ip`           | `true`   | `string` |            |               | EC2 VM instance ip |
| `consul_ip`                  | `true`   | `string` |            |               | Consul Service ip  |
| `node_exporter_service_port` | `true`   | `string` |            |               | Node Exporter port |

### Artifacts

| Name        | Description                         |
| :---------- | :---------------------------------- |
| `create`    | deploy prometheus pushgateway       |
| `configure` | Inject in COnsul and set up Grafana |
