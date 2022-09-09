import argparse
from loguru import logger
from pathlib import Path
import os
from apijet.utils.opfile import load_project_file
from apijet.utils.opfile import update_file_with_content


def add_parser(sub_parsers: argparse):
    create_parser = sub_parsers.add_parser(name='endpoint', help='add an endpoint to the project')
    create_parser.set_defaults(action='endpoint')
    create_parser.add_argument('--add', type=str, help="endpoint name")
    create_parser.add_argument('--remove', type=str, help="endpoint name")
    return sub_parsers


def add(name: str, root_dir: str) -> bool:
    # main folder path
    logger.info(f"{os.getcwd()}")
    project_file_path = f"{root_dir}/apijet.json"
    logger.info(f"Project folder {project_file_path}.")

    # check if in project folder
    if Path(project_file_path).is_file() is False:
        logger.warning("This is not an apiJet project.")
        return False

    project_file = load_project_file(project_file_path)
    logger.info(f"Project {project_file['name']} loaded.")
    project_name = project_file['name']

    update_file_with_content(f"{root_dir}/{project_name}/core/{name}.py", "")
    logger.info(f"Core for {name} endpoint created.")

    update_file_with_content(f"{root_dir}/{project_name}/models/{name}.py", "")
    logger.info(f"Model for {name} endpoint created.")

    update_file_with_content(f"{root_dir}/{project_name}/routers/{name}.py", "")
    logger.info(f"Router for {name} endpoint created.")

    return True
