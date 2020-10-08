# Monitoring Stack and Google Hosted Cloud Function service Templaye

TOSCA Service Template to deploy the RADON Monitoring Stack over a GCP function

---

### Usage

Download the CSAR `EC2_on_AWS.csar` and extract into a new directory.

Initialize xOpera in the same directory:

```
python3 -m venv .venv && . .venv/bin/activate
pip install opera
```

Create a `inputs.yaml` file in the same directory and add the following:

```
vpc_subnet_id: subnet-08d370 # replace with actual value from your AWS setup
ssh_key_name: opera          # name of your certificate in your AWS setup
ssh_key_file: ~/opera.pem    # path to your personal AWS certificate
```

Deployment TOSCA Service Template:

```
# note: adapt path to certificate
OPERA_SSH_USER=ubuntu OPERA_SSH_IDENTITY_FILE=~/opera.pem opera deploy --inputs inputs.yaml _definitions/radonblueprintsexamples__EC2_on_AWS.tosca
```

You can login with SSH to the create instance:

```
ssh -i ~/opera.pem ubuntu@<public ip from aws console>
```

Undeploy instance:

```
opera undeploy
```
