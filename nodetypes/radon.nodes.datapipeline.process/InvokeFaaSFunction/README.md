![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## InvokeFaaSFunction Pipeline Node Type

A node type to invoke a generic FaaS function using HTTP endpoint.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `InvokeFaaSFunction` | `radon.nodes.datapipeline.process.InvokeFaaSFunction` | 1.0.0 | `radon.nodes.datapipeline.process.FaaSFunction` |


Currently this node type is similar to InvokeOpenFaaS node type

This nodetype encode the input to base64 and send a json with following format

```json
{
  "blob_name":"${filename}",
  "body":"base64_encoded_input_file"
}
```

Inside the Azure function, you can access those data in following manner (using Python code)

```python
data_in_base64 = req.get_json().get('body')
blobname = req.get_json().get('blob_name')
```