from tests.integration.build_invoke.build_invoke_base import BuildInvokeBase

"""
For each template, it will test the following sam commands:
1. sam init
2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
"""

class BuildInvoke_nodejs20_x_cookiecutter_aws_sam_hello_nodejs(BuildInvokeBase.SimpleHelloWorldBuildInvokeBase):
    directory = "nodejs20.x/hello"
    # TODO (hawflau): remove after GA
    should_test_lint = False

class BuildInvoke_nodejs20_x_cookiecutter_aws_sam_step_functions_sample_app(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs20.x/step-func"
    # TODO (hawflau): remove after GA
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_from_scratch(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs20.x/scratch"
    # TODO (hawflau): remove after GA
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_cloudwatch_events(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs20.x/cw-event"
    # TODO (hawflau): remove after GA
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_s3(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs20.x/s3"
    # TODO (hawflau): remove after GA
    should_test_lint = False

    # if we want to check response json, we need to setup bucket for testing


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_sns(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs20.x/sns"
    # TODO (hawflau): remove after GA
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_sqs(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs20.x/sqs"
    # TODO (hawflau): remove after GA
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_response_streaming(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs20.x/response-streaming"
    # TODO (hawflau): remove after GA
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_web(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs20.x/web"
    # TODO (hawflau): remove after GA
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_quick_start_full_stack(BuildInvokeBase.QuickStartWebBuildInvokeBase):
    directory = "nodejs20.x/full-stack"
    # TODO (hawflau): remove after GA
    should_test_lint = False


class BuildInvoke_image_nodejs20_x_cookiecutter_aws_sam_hello_nodejs_lambda_image(
    BuildInvokeBase.SimpleHelloWorldBuildInvokeBase
):
    directory = "nodejs20.x/hello-img"
    # TODO (hawflau): remove after GA
    should_test_lint = False


class BuildInvoke_nodejs20_x_cookiecutter_aws_sam_gql_quick_start(BuildInvokeBase.BuildInvokeBase):
    directory = "nodejs20.x/hello-gql"
    should_test_lint = False
