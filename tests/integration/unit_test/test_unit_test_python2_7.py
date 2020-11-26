from tests.integration.base import Base


class UnitTest_python2_7_cookiecutter_aws_sam_hello_python(Base.PythonUnitTestBase):
    python_executable = "python2.7"
    directory = "python2.7/cookiecutter-aws-sam-hello-python"


class UnitTest_python2_7_cookiecutter_aws_sam_step_functions_sample_app(Base.PythonUnitTestBase):
    python_executable = "python2.7"
    directory = "python2.7/cookiecutter-aws-sam-step-functions-sample-app"
