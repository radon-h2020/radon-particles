## Publish to Kaka Topic

This type represents the relationship between a Kafka producer and a Kafka topic.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `PublishToKafkaTopic`   | `radon.relationships.kafka.PublishToKafkaTopic`   | 1.0.0   | `tosca.relationships.ConnectsTo`          |

### Valid Target types

* `radon.capabilities.kafka.KafkaTopic`

### Properties

| Name | Required | Type | Constraint | Default Value| Description |
|:---- |:-------- |:---- |:---------- |:-----------  |:----------- |
| `request_required_acks`   | `true`| `string` |  `valid_values: [ no_ack, leader, in_syncs ]` | `no_ack`| This value controls when a produce request is considered completed. Typical values are: <ul> <li> `no_ack`: producer does not wait. </li> <li> `leader`: producer waits only for the leader broker. </li> <li> `in_syncs`: producer waits for all in-sync brokers. </li></ul> |                                                                                        <li>
| `message_send_max_retries` | `false` | `integer` | `greater_or_equal: 0` | 3 | This property will cause the producer to automatically retry a failed send request. May result in duplicates |
| `retry_backoff` | `false` | `scalar-unit.time` | `greater_or_equal: 0 ms` | 100 ms | This property specifies the amount of time that the producer waits before refreshing the metadata of relevant topics to allow for potential leader election.|
| `request_timeout` | `false` | `scalar-unit.time` | `greater_or_equal: 0 ms` | 10000 ms | This property specifies the amount of time that the producer waits before refreshing the metadata of relevant topics to allow for potential leader election.The amount of time the broker will wait trying to meet the request.required.acks requirement before sending back an error to the client.|

---
