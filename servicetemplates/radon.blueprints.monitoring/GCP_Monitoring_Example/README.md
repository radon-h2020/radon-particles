# Monitoring Stack and Google Hosted Cloud Function service Template

TOSCA Service Template to deploy the RADON Monitoring Stack over a GCP function

---

### Usage

Download the CSAR `GCP_Monitoring.csar` and extract into a new directory.

Initialize xOpera in the same directory:

```
python3 -m venv .venv && . .venv/bin/activate
pip install opera
```

Create a `inputs.yaml` file in the same directory and add the following:

```
host_ip: localhost

user_email: a.sidiropoulos@atc.gr         # vreplace with own e-mail. Email has to be the one declared in keycloak
consul_ip: 3.127.254.144                  # replace with consul ip
pushgateway_service_port: 9091            # pushgateway port
grafana_api_ip: http://3.127.254.144:3100 # Grafana dashboards ip

project_id: pivotal-gearbox-282913               # replace with google project id
service_account_file: /tmp/service_account.json  # it is important to place the service account file in /tmp
bucket_location: us-central1
bucket_in_name: bkt_in_anesid
bucket_out_name: bkt_out_anesid
bucket_function_name: bkt_fnc_anesid
function_name: predict-sentiment-anesid
function_location: us-central1
function_runtime: python37
function_entry_point: entry_point
function_timeout: 480
zip_file: /tmp/function.zip
function_memory: 2048


aws_platform_region: eu-central-1
ec2_image: ami-0b418580298265d5c
ec2_ssh_key_name: push-gateway-key
ec2_vpc_subnet_id: subnet-00268ff84ba97070c
ec2_instance_type: t2.micro
ec2_ssh_key_file: "/tmp/push-gateway-key.pem" # it is important to place your personal .pem file in tmp
ec2_ssh_user: ubuntu
```

In addition it is crucial to place credential file located in ~/.aws directory

Deployment TOSCA Service Template:

```
# note: adapt path to certificate
OPERA_SSH_USER=ubuntu OPERA_SSH_IDENTITY_FILE=/tmp/push-gateway-key.pem opera deploy --inputs inputs.yml --clean-state _definitions/radonnodesmonitoring__GCPMonitoringAgent.yml
```

Undeploy instance:

```
opera undeploy
```
