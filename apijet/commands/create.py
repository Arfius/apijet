from argparse import Namespace
import argparse
from shutil import which
from loguru import logger
from pathlib import Path
import json
from apijet.utils.opfile import update_file_with_content
from apijet.utils.opfile import check_write_permission


def add_parser(sub_parsers: argparse):
    create_parser = sub_parsers.add_parser(name='create', help='Create a new project')
    create_parser.set_defaults(action='create')
    create_parser.add_argument('--port', type=int)
    create_parser.add_argument('--name', type=str)
    return sub_parsers


def create(name: str, port: int, root_dir: str) -> None:

    if check_write_permission(root_dir) is False:
        return False

    main_folder = f"{root_dir}/{name}"
    project_file = f"{main_folder}/{name}.json"

    file_project = {
        'name': name,
        'port': port,
        'folder': main_folder,
        'project_file': project_file
    }

    # check if folder exists
    if Path(main_folder).is_dir():
        logger.warning(f"Folder {main_folder} already exists.")
        return False

    # create folder if not exist
    Path(f"{main_folder}").mkdir()
    logger.info(f"Folder projet: {main_folder} create successfully.")

    # create project folders
    folders = ['core', 'models', 'routers']
    for folder in folders:
        logger.info(f"Folder projet: {main_folder}/{folder} create successfully.")
        Path(f"{main_folder}/{folder}").mkdir()

    # create main.py
    update_file_with_content(f"{main_folder}/app.py", "")

    # save project file in root project folder
    update_file_with_content(project_file, json.dumps(file_project, indent=4))
    return True