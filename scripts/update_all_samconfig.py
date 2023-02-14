"""
Helper script to write the image and zip-based samconfig.toml files to each app template.
"""
import shutil
from pathlib import Path
from typing import Tuple

from common import InitProject, get_runtime_directories, find_cookie_cutter_projects

# These projects already have samconfig.toml files that we don't want to overwrite
SAMCONFIG_IGNORE_LIST = [
    "al2/graalvm/11/maven",
    "al2/graalvm/17/maven",
    "al2/graalvm/11/gradle",
    "al2/graalvm/17/gradle",
]

IMAGE_CONFIG = "configs/samconfig-image.toml"
ZIP_CONFIG = "configs/samconfig-zip.toml"
DEFAULT_CONFIG = "samconfig.toml"


def main():
    """
    Entrypoint running logic to get sam config files, find all project
    directories and copy the correct configs into those directories.
    """
    zip_config, image_config = _samconfigs()
    runtime_directories = get_runtime_directories()
    projects = find_cookie_cutter_projects(runtime_directories)
    for project in projects:
        _copy_config_to_projects(zip_config, image_config, project)


def _copy_config_to_projects(zip_config: Path, image_config: Path, project: InitProject):
    """
    Given the config files and a project, selects which config file to use
    and copies it into the cookie cutter directory of the project.
    """
    if str(project.directory) in SAMCONFIG_IGNORE_LIST:
        return

    project_files_directory = Path(project.directory, project.cookieCutterName)
    app_template = project.directory.stem
    if Path.is_dir(project_files_directory):
        if "img" in app_template:
            shutil.copyfile(image_config, Path(project_files_directory, DEFAULT_CONFIG))
            print(f"Copying image config to {project_files_directory}")
        else:
            shutil.copyfile(zip_config, Path(project_files_directory, DEFAULT_CONFIG))
            print(f"Copying ZIP config to {project_files_directory}")


def _samconfigs() -> Tuple[Path, Path]:
    """
    Function returns the paths to image and zip template samconfig files.
    """
    basepath = Path(__file__).parent
    return _get_zip_toml(basepath), _get_image_toml(basepath)


def _get_image_toml(basepath: str) -> Path:
    """
    Takes a basepath string to the directory containing samconfig template.
    Returns a Path to the image template file.
    """
    return Path(basepath, IMAGE_CONFIG)


def _get_zip_toml(basepath: str) -> Path:
    """
    Takes a basepath string to the directory containing samconfig template.
    Returns a Path to the zip template file.
    """
    return Path(basepath, ZIP_CONFIG)


if __name__ == "__main__":
    main()
