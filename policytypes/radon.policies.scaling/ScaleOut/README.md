## Scale Out Policy

Policy type representing a scale-out configuration for a TOSCA entity.

| Name       | URI                               | Version | Derived From             |
| :--------- | :-------------------------------- | :------ | :----------------------- |
| `ScaleOut` | `radon.policies.scaling.ScaleOut` | 1.0.0   | `tosca.policies.Scaling` |

### Properties

| Name              | Required | Type      | Constraint              | Default Value | Description                                        |
| :---------------- | :------- | :-------- | :---------------------- | :------------ | :------------------------------------------------- |
| `cpu_lower_bound` | `false`  | `float`   | `greater_or_equal: 0.0` |               | The lower bound for the CPU                        |
| `cpu_upper_bound` | `false`  | `float`   | `less_or_equal: 100.0`  |               | The upper bound for the CPU                        |
| `adjustment`      | `false`  | `integer` | `greater_or_equal: 1`   |               | The amount by which to scale                       |
| `ram_upper_bound` | `false`  | `integer` | `less_or_equal: 100.0`  |               | The upper bound for the RAM                        |
| `callbackUrlCPU`  | `false`  | `string`  |                         |               | URL that nadles the scaling request in xOpera SaaS |
