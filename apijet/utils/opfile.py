from asyncio.log import logger
from loguru import logger
from pathlib import Path
import os

def update_file_with_content(file_path:str, content:str):
    try:
        f = open(file_path, "a")
        f.write(content)
        f.close()
        logger.info(f"File {file_path} create successfully.")
    except Exception as e:
        logger.warning(f"Error during write file - {e}.")

def check_write_permission(folder_path:str):
    write_permission = os.access(folder_path, os.W_OK)
    logger.info(f"Folder {folder_path} write permission {write_permission}")
    return write_permission

def remove_project(file_path:str):
    pth = Path(file_path)
    for child in pth.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            remove_project(child)
    pth.rmdir()
    return Path(file_path).is_dir() == False