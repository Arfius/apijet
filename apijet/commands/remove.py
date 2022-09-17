import argparse
from pathlib import Path
from apijet.utils.opfile import remove_project


def add_parser(sub_parsers: argparse):
    create_parser = sub_parsers.add_parser(name='remove', help='Remove a project')
    create_parser.set_defaults(action='remove')
    create_parser.add_argument('--name', type=str, help="project name")
    return sub_parsers


def remove(root_dir: str):
    project_file_path = f"{root_dir}/apijet.json"

    # check if in project folder
    if Path(project_file_path).is_file() is False:
        print("🛑> This is not an apijet project.")
        return False

    if remove_project(root_dir) is True:
        print("ℹ️ > Project removed successfully")
        return True
    else:
        print("🛑> An error is occurred removing project")
        return False
