from apijet.create import create
from apijet.utils.opfile import remove_project
from pathlib import Path


def test_create_projet():
    assert create('test_project', 5083, './') is True


def test_project_folder_structure():
    folders = ['core', 'models', 'routers']
    for folder in folders:
        assert Path(f'./test_project/{folder}').is_dir() is True

    assert Path('./test_project/main.py').is_file() is True


def test_folder_already_exist():
    assert create('test_project', 5083, './') is False
    assert remove_project('./test_project') is True
