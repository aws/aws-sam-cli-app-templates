"""
    Tests cookiecutter baking process and rendered content
"""


def test_project_tree(cookies):
    result = cookies.bake(extra_context={
        'project_name': 'hello sam'
    })
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'hello sam'
    assert result.project.isdir()
    assert result.project.join('.gitignore').isfile()
    assert result.project.join('template.yaml').isfile()
    assert result.project.join('README.md').isfile()
    assert result.project.join('src').isdir()
    assert result.project.join('test').isdir()
    assert result.project.join('src', 'HelloWorldAot').isdir()
    assert result.project.join(
        'src', 'HelloWorldAot', 'HelloWorldAot.csproj').isfile()
    assert result.project.join('src', 'HelloWorldAot', 'Function.cs').isfile()
    assert result.project.join(
        'src', 'HelloWorldAot', 'aws-lambda-tools-defaults.json').isfile()
    assert result.project.join(
        'test', 'HelloWorldAot.Test', 'FunctionTest.cs').isfile()
    assert result.project.join(
        'test', 'HelloWorldAot.Test', 'HelloWorldAot.Tests.csproj').isfile()


def test_app_content(cookies):
    result = cookies.bake(extra_context={'project_name': 'my_lambda'})
    app_file = result.project.join('src', 'HelloWorldAot', 'Function.cs')
    app_content = app_file.readlines()
    app_content = ''.join(app_content)

    contents = (
        "GetCallingIP",
        "GetStringAsync",
        "location",
        "message",
        "hello world",
        "StatusCode"
    )

    for content in contents:
        assert content in app_content
