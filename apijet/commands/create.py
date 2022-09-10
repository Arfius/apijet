import argparse
from loguru import logger
from pathlib import Path
import json
from apijet.utils.opfile import update_file_with_content
from apijet.utils.opfile import check_write_permission
from apijet.utils.opfile import read_template


def add_parser(sub_parsers: argparse):
    create_parser = sub_parsers.add_parser(name='create', help='Create a new project')
    create_parser.set_defaults(action='create')
    create_parser.add_argument('--port', type=int, help="port where apis are exposed")
    create_parser.add_argument('--name', type=str, help="project name")
    create_parser.add_argument('--address', type=str, help="ip address where apis are exposed")
    return sub_parsers


def create(name: str, port: int, address: str, root_dir: str) -> bool:

    # check write permission
    if check_write_permission(root_dir) is False:
        return False

    # main folder path
    main_folder = f"{root_dir}/{name}"

    # check if folder exists
    if Path(main_folder).is_dir():
        logger.warning(f"Folder {main_folder} already exists.")
        return False

    # create folder if not exist
    Path(f"{main_folder}").mkdir()
    logger.info(f"Folder projet: {main_folder} create successfully.")

    # apiJet file configuration
    project_file = f"{main_folder}/apijet.json"
    file_project = {
        'name': name,
        'port': port,
        'address': address,
        'folder': main_folder,
        'project_file': project_file
    }

    # save project file in root project folder
    update_file_with_content(project_file, json.dumps(file_project, indent=4))

    # create project folders
    Path(f"{main_folder}/{name}").mkdir()
    logger.info(f"Folder projet: {main_folder} create successfully.")

    folders = ['core', 'models', 'routers', 'database']
    for folder in folders:
        logger.info(f"Folder projet: {main_folder}/{name}/{folder} create successfully.")
        Path(f"{main_folder}/{name}/{folder}").mkdir()

    # create main.py
    app_content = read_template('app')
    app_content = app_content.format(address=address, port=port)
    update_file_with_content(f"{main_folder}/{name}/app.py", app_content)

    return True
