from pathlib import Path
from common import get_runtime_directories, find_cookie_cutter_projects


def main():
    runtime_directories = get_runtime_directories()
    cookie_cutter_projects = find_cookie_cutter_projects(runtime_directories)

    for project in cookie_cutter_projects:
        config_path = Path(project[0], project[1], "samconfig.toml")
        if not config_path.is_file():
            print(f"No samconfig.toml file found in {config_path}")
            exit(1)
    print("All cookie cutter projects contain a samconfig.toml file.")


if __name__ == "__main__":
    main()
