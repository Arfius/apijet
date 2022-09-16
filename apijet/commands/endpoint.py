import argparse
from loguru import logger
from pathlib import Path
import os
from apijet.utils.opfile import load_project_file
from apijet.utils.opfile import update_file_with_content
from apijet.utils.opfile import read_template
from apijet.utils.opfile import append_text_to_file_with_key


def add_parser(sub_parsers: argparse):
    create_parser = sub_parsers.add_parser(name='endpoint', help='Add or Remove an endpoint to the project')
    create_parser.set_defaults(action='endpoint')
    create_parser.add_argument('--add', type=str, help="endpoint name")
    create_parser.add_argument('--database', action='store_true', help="endpoint name")
    create_parser.add_argument('--remove', type=str, help="endpoint name")
    return sub_parsers


def add(name: str, root_dir: str, database:bool) -> bool:
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
    collection = name

    if database:
        database_content = read_template('database')
        database_content = database_content.format(collection=collection, project_name=project_name)
        update_file_with_content(f"{root_dir}/{project_name}/database/{name}.py", database_content)
        logger.info(f"Collection Manager for {name} endpoint created.")

    has_db = '_db' if database else ''
    core_content = read_template(f'core{has_db}')
    core_content = core_content.format(endpoint_name=collection, project_name=project_name)
    update_file_with_content(f"{root_dir}/{project_name}/core/{name}.py", core_content)
    logger.info(f"Core for {name} endpoint created.")

    model_content = read_template(f'model{has_db}')
    model_content = model_content.format(endpoint_name=collection, project_name=project_name)
    update_file_with_content(f"{root_dir}/{project_name}/models/{name}.py", model_content)
    logger.info(f"Model for {name} endpoint created.")

    router_content = read_template(f'router{has_db}')
    router_content = router_content.format(endpoint_name=collection, project_name=project_name)
    update_file_with_content(f"{root_dir}/{project_name}/routers/{name}.py", router_content)
    logger.info(f"Router for {name} endpoint created.")

    append_text_to_file_with_key(f"{root_dir}/{project_name}/app.py", "apijet-router-import",
                                    f"from routers.{name} import {name}_router")

    append_text_to_file_with_key(f"{root_dir}/{project_name}/app.py", "apijet-router-include",
                                    f"app.include_router({name}_router)")
    return True
