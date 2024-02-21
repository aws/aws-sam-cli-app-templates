# AWS SAM CLI Application Templates

This repository contains the application templates used in the AWS SAM CLI for `sam init` calls.

## Contributing

We welcome issue reports and pull requests to help improve these application templates.

### Testing a template locally

You can create a buildable and deployable project folder from a local template using the below command. The `<project_name>` can be whatever you want your project to be called, and `<path/to/init_template>` should point to the existing folder that contains the template.

Command: `sam init --no-input --location <path/to/init_template> --name <project_name>`

For example: `samdev init --no-input --location /home/myuser/code/aws-sam-cli-app-templates/dotnet8/hello-native-aot --name beauNativeAotTest`

### Testing updated `sam init` locally

To test an updated workflow of `sam init`, including changes to the prompts to create your new template, you need to push your changes from your fork so they can be downloaded by the SAM CLI. You'll also need a local copy of SAM CLI's source code to modify to point to your fork. Follow SAM CLI's main [DEVELOPMENT_GUIDE.md](https://github.com/aws/aws-sam-cli/blob/develop/DEVELOPMENT_GUIDE.md) to get a local version of SAM CLI setup. With your fork pushed, you can update the [samcli/commands/init/init_templates.py](https://github.com/aws/aws-sam-cli/blob/49fb8f9ad60d1daee67ebc8045266c965a125b3c/samcli/commands/init/init_templates.py#L38-L42) file in your local SAM CLI like below. Make sure to update all three variables.

```
APP_TEMPLATES_REPO_COMMIT = <the commit hash>
MANIFEST_URL = (
    f"https://raw.githubusercontent.com/<your_github_id>/aws-sam-cli-app-templates/{APP_TEMPLATES_REPO_COMMIT}/manifest-v2.json"
)
APP_TEMPLATES_REPO_URL = "https://github.com/<your_github_id>/aws-sam-cli-app-templates"
```

Example
```
APP_TEMPLATES_REPO_COMMIT = "abcdefg1234567d6e78f319e189d39593c628b7f"
MANIFEST_URL = (
    f"https://raw.githubusercontent.com/aws/aws-sam-cli-app-templates/abcdefg1234567d6e78f319e189d39593c628b7f/manifest-v2.json"
)
APP_TEMPLATES_REPO_URL = "https://github.com/cool-developer-xyz/aws-sam-cli-app-templates"
```

## License

This project is licensed under the Apache-2.0 License.

