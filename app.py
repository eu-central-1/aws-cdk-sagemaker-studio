#!/usr/bin/env python3

from aws_cdk import core as cdk

from sagemakerStudioCDK.sagemaker_studio_stack import SagemakerStudioStack
import os
# import boto3

# sts_client = boto3.client("sts")
# account_id = os.environ.get('CDK_DEFAULT_ACCOUNT', sts_client.get_caller_identity()["Account"])
# region = os.environ.get('CDK_DEFAULT_REGION', 'eu-central-1')

# For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
env = cdk.Environment(
    account=os.getenv('CDK_DEFAULT_ACCOUNT'),
    region=os.getenv('CDK_DEFAULT_REGION', 'eu-central-1')
)

app = cdk.App()
# SagemakerStudioStack(app, "sagemakerStudioCDK", env={"account": account_id, 'region': region})
SagemakerStudioStack(app, "sagemakerStudioCDK", env=env)

app.synth()
