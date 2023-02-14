"""
Python script to check if the projects in the repository match those listed in the manifest.
"""
from common import InitProject, find_cookie_cutter_projects, get_runtime_directories, get_templates_in_manifest
from typing import List

# TODO: Turn this script into a GitHub action running against PRs to ensure parity between what's in the repo and what's in the manifest.


def main():
    """
    Entrypoint function to check get projects in manifest 
    and in the repo and check for any discrepencies.
    """
    runtime_directories = get_runtime_directories()
    directory_traversal_projects: List[InitProject] = find_cookie_cutter_projects(runtime_directories)
    manifest_projects: List[InitProject] = get_templates_in_manifest()
    directory_traversal_paths = list(map(lambda project: str(project.directory), directory_traversal_projects))
    manifest_paths = list(map(lambda project: str(project.directory), manifest_projects))
    print("Checking that all projects in the manifest are also in the repository")
    _check_difference(manifest_paths, directory_traversal_paths)
    print("Checking that all projects in the repository are also in the manifest")
    _check_difference(directory_traversal_paths, manifest_paths)


def _check_difference(list_a, list_b):
    """
    Helper function to check if an item in list a is not in list b
    """
    diff = [x for x in list_a if x not in list_b]
    if diff:
        print("Discrepency found between lists:")
        print(diff)
        exit(1)


if __name__ == "__main__":
    main()
