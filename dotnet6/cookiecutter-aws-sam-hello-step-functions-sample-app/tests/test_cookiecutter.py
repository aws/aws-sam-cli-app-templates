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

    assert result.project.join('statemachine').isdir()
    assert result.project.join(
        'statemachine', 'stockTrader.asl.json').isfile()

    assert result.project.join('functions').isdir()
    assert result.project.join('functions', 'StockBuyer').isdir()
    assert result.project.join(
        'functions', 'StockBuyer', 'StockBuyer.csproj').isfile()
    assert result.project.join('functions', 'StockBuyer', 'Function.cs').isfile()
    assert result.project.join(
        'functions', 'StockBuyer', 'aws-lambda-tools-defaults.json').isfile()
    assert result.project.join('functions', 'StockChecker').isdir()
    assert result.project.join(
        'functions', 'StockChecker', 'StockChecker.csproj').isfile()
    assert result.project.join('functions', 'StockChecker', 'Function.cs').isfile()
    assert result.project.join(
        'functions', 'StockChecker', 'aws-lambda-tools-defaults.json').isfile()
    assert result.project.join('functions', 'StockSeller').isdir()
    assert result.project.join(
        'functions', 'StockSeller', 'StockSeller.csproj').isfile()
    assert result.project.join('functions', 'StockSeller', 'Function.cs').isfile()
    assert result.project.join(
        'functions', 'StockSeller', 'aws-lambda-tools-defaults.json').isfile()

    assert result.project.join('test').isdir()
    assert result.project.join(
        'test', 'StockBuyer.Test', 'FunctionTest.cs').isfile()
    assert result.project.join(
        'test', 'StockBuyer.Test', 'StockBuyer.Tests.csproj').isfile()
    assert result.project.join(
        'test', 'StockChecker.Test', 'FunctionTest.cs').isfile()
    assert result.project.join(
        'test', 'StockChecker.Test', 'StockChecker.Tests.csproj').isfile()
    assert result.project.join(
        'test', 'StockSeller.Test', 'FunctionTest.cs').isfile()
    assert result.project.join(
        'test', 'StockSeller.Test', 'StockSeller.Tests.csproj').isfile()
