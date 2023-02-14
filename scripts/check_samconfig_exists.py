"""
Python function to check that all app templates include a samconfig.toml file.
Used by the samconfig-check GitHub action.
"""
from pathlib import Path
from common import InitProject, get_runtime_directories, find_cookie_cutter_projects
from typing import List


def main():
    """
    Entrypoint function to read get all project directories and check
    to ensure all app template directory includes a samconfig.toml file.
    """
    runtime_directories = get_runtime_directories()
    cookie_cutter_projects: List[InitProject] = find_cookie_cutter_projects(runtime_directories)

    for project in cookie_cutter_projects:
        config_path = Path(project.directory, project.cookieCutterName, "samconfig.toml")
        if not config_path.is_file():
            print(f"No samconfig.toml file found in {config_path}")
            exit(1)
    print("All cookie cutter projects contain a samconfig.toml file.")


if __name__ == "__main__":
    main()
