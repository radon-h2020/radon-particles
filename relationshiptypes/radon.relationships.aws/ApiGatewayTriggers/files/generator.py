import json
import sys
import os

endpoint_def = '{ "responses": { "200": { "description": "200 response"}, "400": { "description": "bad input parameter"}}, "x-amazon-apigateway-integration": { "responses": { "default": { "statusCode": "200" }}, "uri": "$FUNCTION_ARN$", "passthroughBehavior": "when_no_match", "httpMethod": "POST", "contentHandling": "CONVERT_TO_TEXT", "type": "aws_proxy", "credentials": "$AWS_ROLE$" } }'
arn = "arn:aws:apigateway:REGION:lambda:path/2015-03-31/functions/FUNCTION_ARN/invocations"


def update_spec(path, endpoint, method_csv, region, function_arn, role):
    with open(path, "r") as jsonFile:
        spec = json.load(jsonFile)

    new_block = generate_endpoint(region, function_arn, role)
    if endpoint not in spec['paths']:
        spec['paths'][endpoint] = {}

    methods = split_methods(method_csv)

    for method in methods:
        method = method.lower()
        if method not in spec['paths'][endpoint]:
            spec['paths'][endpoint][method] = {}
        spec['paths'][endpoint][method] = new_block

    with open(path, "w") as jsonFile:
        json.dump(spec, jsonFile)


def generate_endpoint(region, function_arn, role):
    constructed_arn = arn.replace('REGION', region).replace('FUNCTION_ARN', function_arn)
    endpoint_dict = json.loads(endpoint_def)
    endpoint_dict['x-amazon-apigateway-integration']['uri'] = constructed_arn
    endpoint_dict['x-amazon-apigateway-integration']['credentials'] = role
    return endpoint_dict


def split_methods(method_csv):
    return method_csv.strip().split(',')


def main():
    print(sys.argv)
    if len(sys.argv) < 7:
        sys.exit("Not enough args")
    update_spec(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])


if __name__ == "__main__":
    main()
