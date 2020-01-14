## Google Cloud Triggers Relationship

Google Cloud-specific relationship type representing GCResource-to-GCFunction communication.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `GoogleTriggers` | `radon.relationships.google.GoogleTriggers` | 1.0.0 | `radon.relationships.abstract.Triggers` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
|`events`|`true`|list of `radon.datatypes.Event`|`length: 1`|   | The event associated with this relationship |

### Notes

* The following parameters are added to tht inputs of the `Configure` interface:
    * `EVENT`: taken from the `events` property
    * `RESOURCE`: the `name` of the `SOURCE` Google Cloud Resource
* A template of this type should provide implementation artifacts that deploy the Cloud Function specified at the `TARGET` side.
