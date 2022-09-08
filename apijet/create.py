from loguru import logger
from pathlib import Path
import json 
from apijet.utils.opfile import update_file_with_content
from apijet.utils.opfile import check_write_permission


def create(name:str, port:int, root_dir:str) -> None:

    if check_write_permission(root_dir) is False:
        return False

    folder= f"{root_dir}/{name}"
    project_file= f"{folder}/{name}.json"

    file_project = {
        'name':name,
        'port':port,
        'folder':folder,
        'project_file':project_file
    }
    
    #check if folder exists
    if Path(folder).is_dir():
        logger.warning(f"Folder {folder} already exists.")
        return False

    #create folder if not exist
    Path(f"{folder}").mkdir()
    logger.info(f"Folder projet: {folder} create successfully.")

    #save project file in root project folder
    update_file_with_content(project_file, json.dumps(file_project, indent = 4))
    return True
