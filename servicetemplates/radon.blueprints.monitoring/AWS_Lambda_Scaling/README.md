# AWS Lambda Monitoring and Scaling Service Template.

TOSCA Service Template to deploy the RADON Monitoring Stack over an AWS function.
Alerting and Scaling of the Lambda function is implemented through a new interface - policy

---

### Usage

Download the CSAR `AWSScalableLambda_w1-wip1.csar` and upload it on xOper Saas

Create a callback URL in xOpera SaaS

Create a `inputs.yaml` file in the same directory and add the following:

```
callbackUrlCPU: << Callback URL >>

```
