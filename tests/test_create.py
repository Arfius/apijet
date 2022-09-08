from apijet.commands.create import create
from apijet.commands.create import add_parser
from apijet.utils.opfile import remove_project
from pathlib import Path
import argparse


def test_parser():
    parser = argparse.ArgumentParser(description='Testing apiJet perser')
    sub_parsers = parser.add_subparsers(title="Actions")
    add_parser(sub_parsers)
    name_space = parser.parse_args(['create', '--port', '1234', '--name', 'test_project'])
    assert name_space.port == 1234
    assert name_space.name == 'test_project'


def test_create_projet():
    assert create('test_project', 5083, './') is True


def test_project_folder_structure():
    folders = ['core', 'models', 'routers']
    for folder in folders:
        assert Path(f'./test_project/{folder}').is_dir() is True

    assert Path('./test_project/app.py').is_file() is True


def test_folder_already_exist():
    assert create('test_project', 5083, './') is False
    assert remove_project('./test_project') is True
