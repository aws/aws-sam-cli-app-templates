# Cookiecutter SAM for Amazon EventBridge Java Lambda functions



This is a [Cookiecutter](https://github.com/audreyr/cookiecutter) template to create an Amazon EventBridge Starter App based on Serverless Application Model (SAM) and Java.

It is important to note that you should not try to `git clone` this project, nor use `cookiecutter` CLI as with other SAM templates. Normally, ``{{cookiecutter.project_name}}`` will be rendered based on your input and therefore all variables and files will be rendered properly.

However, in addition to that, this SAM template depends on dynamically generated code from schemas provided as a parameter.

Instead of running `cookiecutter` on this template directly, please instead install the `aws sam cli`, and run `sam init` 

## Requirements

Install `https://github.com/awslabs/aws-sam-cli` command line:

## Usage

Generate a new SAM based Serverless App: `sam init`, then choose the `"AWS SAM EventBridge App from Scratch (for any Event Trigger)"` template to enable specific schema selection.

You'll be prompted a few questions to help this cookiecutter template to scaffold this project and after its completed you should see a new folder at your current path with the name of the project you gave as input.



# Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)


License
-------

This project is licensed under the terms of the [MIT License with no attribution](/LICENSE)
