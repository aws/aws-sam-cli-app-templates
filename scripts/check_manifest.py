from common import find_cookie_cutter_projects, get_runtime_directories, get_templates_in_manifest


def main():
    runtime_directories = get_runtime_directories()
    projects = find_cookie_cutter_projects(runtime_directories)
    _check_remaining_templates(projects)


def _check_remaining_templates(projects):
    template_projects = get_templates_in_manifest()
    project_paths = list(map(lambda project: str(project[0]), projects))
    manifest_paths = list(map(lambda project: str(project[0]), template_projects))
    file_diff = [x for x in project_paths if x not in manifest_paths]
    print(file_diff)


if __name__ == "__main__":
    main()
