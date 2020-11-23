from contextlib import contextmanager

import os
import subprocess


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def test_project_tree(cookies):
    result = cookies.bake(extra_context={'project_name': 'test_project'})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'test_project'

    assert result.project.isdir()
    assert result.project.join('README.md').isfile()
    assert result.project.join('template.yaml').isfile()
    assert result.project.join('statemachines').isdir()
    assert result.project.join('functions').isdir()
    assert result.project.join('functions', 'stockBuyer').isdir()
    assert result.project.join('functions', 'stockChecker').isdir()
    assert result.project.join('functions', 'stockSeller').isdir()

    assert result.project.join('functions', 'stockBuyer').join('main.go').isfile()
    assert result.project.join('functions', 'stockBuyer').join('main_test.go').isfile()
    assert result.project.join('functions', 'stockChecker').join('main.go').isfile()
    assert result.project.join('functions', 'stockChecker').join('main_test.go').isfile()
    assert result.project.join('functions', 'stockSeller').join('main.go').isfile()
    assert result.project.join('functions', 'stockSeller').join('main_test.go').isfile()


def test_app_template_content(cookies):
    result = cookies.bake(extra_context={'project_name': 'test_project'})
    app_file = result.project.join('template.yaml')
    app_content = app_file.readlines()
    app_content = ''.join(app_content)

    contents = (
        "Runtime: go1.x",
        "StockSellerFunction",
        "StockBuyerFunction",
        "StockCheckerFunction",
        "StockTradingStateMachine"
    )

    for content in contents:
        assert content in app_content
