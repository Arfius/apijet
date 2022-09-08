from apijet.create import create
from apijet.utils.opfile import remove_project


def test_create_projet():
    assert create('test_project', 5083, './') is True


def test_folder_already_exist():
    assert create('test_project', 5083, './') is False
    assert remove_project('./test_project') is True
