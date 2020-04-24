### Prerequisites:

##### 1. Install boto3, botocore:

```
pip install opera
pip install boto3
pip install botocore
```

##### 2. Move policy.json and function zip to /tmp/ folder

##### 3. Set AWS credentials:

`aws configure` \
or
```
export AWS_ACCESS_KEY_ID=EXAMPLEACCESSKEY
export AWS_SECRET_ACCESS_KEY=EXAMPLESECRETKEY
```

#### Run with:
`opera deploy servicetemplates/radon.blueprints/ImageResize/ServiceTemplate.tosca`
