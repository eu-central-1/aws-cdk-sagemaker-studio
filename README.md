# Build and automatize the management of your Sagemaker Studio Users using AWS CDK!

You should explore the contents of this project. It demonstrates a CDK app with an instance of a
stack (`sagemakerStudioCDK`)

## How it Works

This project uses a simple structure for sources, tooling and testing.
Just execute `make` to see what you can do.

## How to start

You will need to have Python 3.8 installed. After this you just need to call
 ```
 $ make install
 ```

The initialization process also creates a virtualenv within this project, stored under the venv directory.
It will also install AWS cdk command by calling `npm install -g aws-cdk`.

### Python

It is tested with Python 3.8.x.
You can use `make .venv` to create Python environment for this project.

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `make install`
command.

### PyTest

Project uses PyTest for a simple testing approach.
For reference visit: https://docs.pytest.org/en/latest/index.html

### AWS CDK

At this point you can now synthesize the CloudFormation template for this code.

`cdk synth`

After this, use deploy command to deploy CloudFormation stack.

`cdk deploy`

Review the resources that AWS CDK creates for you in your AWS account and choose yes to deploy the stack.

![Diagram](img/aws_cdk_sagemake_studio_deploy_confimation.png)

Wait for your stack to be deployed by checking the status on the AWS CloudFormation console.

Enjoy!

## Useful commands

* `cdk ls`          list all stacks in the app
* `cdk synth`       emits the synthesized CloudFormation template
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk docs`        open CDK documentation

## Cleanup

Follow this step to remove the resources that were deployed in this post.

`cdk destroy`

When asked to confirm the deletion of the four stacks, select “`y`”.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

