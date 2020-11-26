from tests.integration.base import Base


class BuildInvoke_go1_x_cookiecutter_aws_sam_hello_golang(Base.BuildInvokeBase):
    use_container = False
    directory = "go1.x/cookiecutter-aws-sam-hello-golang"


class BuildInvoke_go1_x_cookiecutter_aws_sam_hello_step_functions_sample_app(Base.BuildInvokeBase):
    use_container = False
    directory = "go1.x/cookiecutter-aws-sam-hello-step-functions-sample-app"
