"""
File containing helper functions to perform operations on the repository.
"""
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import List

COOKIE_CUTTER_PROJECT_NAMES = [
    "{{cookiecutter.project_name}}",
    "{{ cookiecutter.project_name }}",
    "{{ cookiecutter.project_slug }}",
]

NON_RUNTIME_DIRECTORY = [
    "tests",
    "scripts",
    "buildspecs",
    ".github",
    ".git",
    ".pytest_cache",
]


@dataclass
class InitProject:
    directory: Path
    cookieCutterName: str


def find_cookie_cutter_projects(runtime_directories: List[str]) -> List[InitProject]:
    """
    Takes a list of runtime directories to look through and recursively
    traverses each directory tree to find all cookie cutter projects.

    Returns a list of Init projects.
    """
    projects = []

    def _traverse(directory):
        directory_files = os.listdir(directory)
        name = _get_project_name(directory_files)
        if name:
            project = InitProject(directory=directory, cookieCutterName=name)
            projects.append(project)
            return

        for file in directory_files:
            file_path = Path(directory, file)
            if Path.is_dir(file_path):
                _traverse(file_path)

    for directory in runtime_directories:
        _traverse(directory)

    return projects


def _get_project_name(project_files: List[str]) -> str:
    """
    Function takes a list of files in a directory and returns the name
    of the cookie cutter directory within it.

    Returns None if no cookie cutter directories are found.
    """
    for project_name in COOKIE_CUTTER_PROJECT_NAMES:
        if project_name in project_files:
            return project_name
    return None


def get_runtime_directories() -> List[str]:
    """
    Get a list of all the runtime directories in the project.
    """
    parent_dir = Path(__file__).parent.parent

    def _runtime_dir_filter(dir):
        return Path.is_dir(Path(dir)) and dir not in NON_RUNTIME_DIRECTORY

    return list(filter(_runtime_dir_filter, os.listdir(parent_dir)))


def get_templates_in_manifest() -> List[InitProject]:
    """
    Reads the manifest file to find all projects listed there
    and returns a list of Init Projects.
    """
    root_dir = Path(__file__).parent.parent
    manifest = Path(root_dir, "manifest-v2.json")
    with open(manifest, "r") as f:
        manifest_json = json.load(f)
    template_projects = []
    for _, templates in manifest_json.items():
        for template in templates:
            directory = Path(template.get("directory"))
            project_files = os.listdir(directory)
            cookie_cutter_name = _get_project_name(project_files)
            project = InitProject(directory=directory, cookieCutterName=cookie_cutter_name)
            template_projects.append(project)
    return template_projects
