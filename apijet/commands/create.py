import argparse
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

    # sanitise project name
    name = name.strip().replace(' ', '_')

    # check write permission
    if check_write_permission(root_dir) is False:
        return False

    # check if already in a project folder
    if Path(f"{root_dir}/apijet.json").is_file() is True:
        print("🛑> You are in an apijet project folder.")
        return False

    # main folder path
    main_folder = f"{root_dir}/{name}"

    # check if folder exists
    if Path(main_folder).is_dir():
        print(f"🛑> Folder {main_folder} already exists.")
        return False

    # create folder if not exist
    Path(f"{main_folder}").mkdir()
    print(f"ℹ️ > Folder projet: {main_folder} create successfully.")

    # apijet file configuration
    project_file = f"{main_folder}/apijet.json"
    file_project = {
        'name': name,
        'port': port,
        'address': address,
        'version': "0.0.1",
        'workers': 1,
        'mongo': {
            'auth': False,
            'address': '127.0.0.1',
            'port': 27017,
            'username': '',
            'password': ''
        },
        'endpoints': []
    }

    # save project file in root project folder
    update_file_with_content(project_file, json.dumps(file_project, indent=4))

    # create project folders
    Path(f"{main_folder}/{name}").mkdir()
    print(f"ℹ️ > Folder projet: {main_folder} create successfully.")

    folders = ['core', 'models', 'routers', 'repository']
    for folder in folders:
        print(f"ℹ️ > Folder projet: {main_folder}/{name}/{folder} create successfully.")
        Path(f"{main_folder}/{name}/{folder}").mkdir()
        update_file_with_content(f"{main_folder}/{name}/{folder}/__init__.py", "")

    # create app.py
    app_content = read_template('app')
    app_content = app_content.format(project_name=name)
    update_file_with_content(f"{main_folder}/{name}/app.py", app_content)
    update_file_with_content(f"{main_folder}/{name}/__init__.py", "")

    # create dbmanager.py
    app_content = read_template('dbmanager')
    app_content = app_content.format(project_name=name)
    update_file_with_content(f"{main_folder}/{name}/repository/dbmanager.py", app_content)

    # create pyobjectid.py
    app_content = read_template('pyobjectid')
    app_content = app_content.format(database_name=name)
    update_file_with_content(f"{main_folder}/{name}/repository/pyobjectid.py", app_content)

    # create message_db.py
    app_content = read_template('message_db')
    app_content = app_content.format(database_name=name)
    update_file_with_content(f"{main_folder}/{name}/models/message_db.py", app_content)

    # create info.py
    app_content = read_template('project')
    update_file_with_content(f"{main_folder}/{name}/project.py", app_content)

    return True
