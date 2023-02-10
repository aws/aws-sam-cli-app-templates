"""
Helper script to write the image and zip-based samconfig.toml files to each app template.
"""
import shutil
from pathlib import Path

from common import get_runtime_directories, find_cookie_cutter_projects

SAMCONFIG_IGNORE_LIST = [
    "al2/graalvm/11/maven",
    "al2/graalvm/17/maven",
    "al2/graalvm/11/gradle",
    "al2/graalvm/17/gradle"
]

IMAGE_CONFIG = "samconfig-image.toml"
ZIP_CONFIG = "samconfig-zip.toml"


def main():
    zip_config, image_config = _samconfigs()
    runtime_directories = get_runtime_directories()
    projects = find_cookie_cutter_projects(runtime_directories)
    for project in projects:
        _copy_config_to_projects(zip_config, image_config, project)


def _copy_config_to_projects(zip_config, image_config, project):
    if str(project[0]) in SAMCONFIG_IGNORE_LIST:
        # These projects already have samconfig.toml files that we don't want to overwrite
        return
    project_files_directory = Path(project[0], project[1])
    app_template = project[0].stem
    if Path.is_dir(project_files_directory):
        if "img" in app_template:
            shutil.copyfile(image_config, Path(project_files_directory, "samconfig.toml"))
            print(f"Copying image config to {project_files_directory}")
        else:
            shutil.copyfile(zip_config, Path(project_files_directory, "samconfig.toml"))
            print(f"Copying ZIP config to {project_files_directory}")


def _samconfigs():
    basepath = Path(__file__).parent
    return _get_zip_toml(basepath), _get_image_toml(basepath)


def _get_image_toml(basepath):
    return Path(basepath, IMAGE_CONFIG)


def _get_zip_toml(basepath):
    return Path(basepath, ZIP_CONFIG)


if __name__ == "__main__":
    main()
