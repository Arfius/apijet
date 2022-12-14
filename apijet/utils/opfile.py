from pathlib import Path
import os
import json


def update_file_with_content(file_path: str, content: str) -> None:
    try:
        f = open(file_path, "w")
        f.write(content)
        f.close()
        print(f"ℹ️ > File {file_path} create successfully.")
    except Exception as e:
        print(f"🛑> Error during write file - {e}.")


def check_write_permission(folder_path: str) -> bool:
    write_permission = os.access(folder_path, os.W_OK)
    print(f"ℹ️ > Folder {folder_path} write permission {write_permission}")
    return write_permission


def remove_project(file_path: str) -> bool:
    pth = Path(file_path)
    for child in pth.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            remove_project(child)
    pth.rmdir()
    return Path(file_path).is_dir() is False


def load_project_file(file_path: str) -> dict:
    return json.loads(open(file_path, "r").read())


def read_template(template_name: str) -> str:
    path = f"{os.path.dirname(__file__)}/../templates/{template_name}.template.py"
    print(f"ℹ️ > {path}")
    return open(path, "r").read()


def append_text_to_file_with_key(file_path, key, text):
    file_content = open(file_path, "r").readlines()
    for x in range(0, len(file_content)):
        if key in file_content[x]:
            file_content.insert(x+1, text+'\n')
            break
    content = ''.join(file_content)
    update_file_with_content(file_path, content)


def remove_text_from_file_by_text(file_path, text):
    file_content = open(file_path, "r").readlines()
    for x in range(0, len(file_content)):
        if text in file_content[x]:
            file_content[x] = ""
            break
    content = ''.join(file_content)
    update_file_with_content(file_path, content)


def remove_file(file_path):
    try:
        path = Path(file_path)
        if path.is_file():
            os.remove(file_path)
            return True
        return False
    except Exception as e:
        print(f"🛑> Error during removing file - {e}.")
        return False
