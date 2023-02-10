import json
import os
from pathlib import Path

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


def find_cookie_cutter_projects(runtime_directories):
    projects = []
    def _traverse(directory):
        directory_files = os.listdir(directory)
        name = _get_project_name(directory_files)
        if name:
            projects.append((directory, name))
            return

        for file in directory_files:
            file_path = Path(directory, file)
            if Path.is_dir(file_path):
                _traverse(file_path)

    for directory in runtime_directories:
        _traverse(directory)
    
    return projects


def _get_project_name(project_files):
    for project_name in COOKIE_CUTTER_PROJECT_NAMES:
        if project_name in project_files:
            return project_name
    return None


def get_runtime_directories():
    parent_dir = Path(__file__).parent.parent
    def _runtime_dir_filter(dir):
        return Path.is_dir(Path(dir)) and dir not in NON_RUNTIME_DIRECTORY
    return list(filter(_runtime_dir_filter, os.listdir(parent_dir)))


def get_templates_in_manifest():
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
            template_projects.append((directory, cookie_cutter_name))
    return template_projects
