import argparse
from pathlib import Path
import os
import json
from apijet.utils.opfile import load_project_file
from apijet.utils.opfile import update_file_with_content
from apijet.utils.opfile import read_template
from apijet.utils.opfile import remove_file
from apijet.utils.opfile import append_text_to_file_with_key
from apijet.utils.opfile import remove_text_from_file_by_text


def add_parser(sub_parsers: argparse):
    create_parser = sub_parsers.add_parser(name='endpoint', help='Add or Remove an endpoint\
to the project')
    create_parser.set_defaults(action='endpoint')
    create_parser.add_argument('--add', type=str, help="endpoint name")
    create_parser.add_argument('--database', action='store_true', help="say that the endpoint\
 needs database support")
    create_parser.add_argument('--remove', type=str, help="not supported yet")
    return sub_parsers


def add(name: str, root_dir: str, database: bool) -> bool:
    # main folder path
    print(f"ℹ️ > {os.getcwd()}")
    project_file_path = f"{root_dir}/apijet.json"
    print(f"ℹ️ > Project folder {project_file_path}.")

    # check if in project folder
    if Path(project_file_path).is_file() is False:
        print("🛑> This is not an apijet project.")
        return False

    project_file = load_project_file(project_file_path)

    if name in project_file["endpoints"]:
        print("🛑> This endpoint already exist.")
        return False

    print(f"ℹ️ > Project {project_file['name']} loaded.")
    project_name = project_file['name']
    collection = name

    if database:
        database_content = read_template('database')
        database_content = database_content.format(collection=collection,
                                                   project_name=project_name)
        update_file_with_content(f"{root_dir}/{project_name}/repository/{name.lower()}.py",
                                 database_content)
        print(f"ℹ️ > Collection Manager for {name} endpoint created.")

    has_db = '_db' if database else ''
    core_content = read_template(f'core{has_db}')
    core_content = core_content.format(endpoint_name=collection, project_name=project_name,
                                       import_name=collection.lower())

    update_file_with_content(f"{root_dir}/{project_name}/core/{name.lower()}.py", core_content)
    print(f"ℹ️ > Core for {name} endpoint created.")

    model_content = read_template(f'model{has_db}')
    model_content = model_content.format(endpoint_name=collection, project_name=project_name)
    update_file_with_content(f"{root_dir}/{project_name}/models/{name.lower()}.py", model_content)
    print(f"ℹ️ > Model for {name} endpoint created.")

    router_content = read_template(f'router{has_db}')
    router_content = router_content.format(endpoint_name=collection, project_name=project_name,
                                           import_name=collection.lower())
    update_file_with_content(f"{root_dir}/{project_name}/routers/{name.lower()}.py",
                             router_content)
    print(f"ℹ️ > Router for {name} endpoint created.")

    append_text_to_file_with_key(f"{root_dir}/{project_name}/app.py", "apijet-router-import",
                                 f"from {project_name}.routers.{name.lower()} import {name}_router")

    append_text_to_file_with_key(f"{root_dir}/{project_name}/app.py", "apijet-router-include",
                                 f"app.include_router({name}_router)")

    # save project file in root project folder
    project_file['endpoints'].append(name)
    update_file_with_content(project_file_path, json.dumps(project_file, indent=4))

    return True


def remove(name: str, root_dir: str):

    # main folder path
    print(f"ℹ️ > {os.getcwd()}")
    project_file_path = f"{root_dir}/apijet.json"
    print(f"ℹ️ > Project folder {project_file_path}.")

    # check if in project folder
    if Path(project_file_path).is_file() is False:
        print("🛑> This is not an apijet project.")
        return False

    project_file = load_project_file(project_file_path)
    project_name = project_file['name']

    if name in project_file["endpoints"]:
        remove_file(f"{root_dir}/{project_name}/repository/{name.lower()}.py")
        remove_file(f"{root_dir}/{project_name}/core/{name.lower()}.py")
        remove_file(f"{root_dir}/{project_name}/models/{name.lower()}.py")
        remove_file(f"{root_dir}/{project_name}/routers/{name.lower()}.py")
        print("ℹ️> Files removed")

        remove_text_from_file_by_text(
                f"{root_dir}/{project_name}/app.py",
                f"from {project_name}.routers.{name.lower()} import {name}_router")

        remove_text_from_file_by_text(
                f"{root_dir}/{project_name}/app.py",
                f"app.include_router({name}_router)")

        # save project file in root project folder
        project_file['endpoints'].remove(name)
        update_file_with_content(project_file_path, json.dumps(project_file, indent=4))
    else:
        return False

    return True
