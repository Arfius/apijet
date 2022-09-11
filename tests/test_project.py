from apijet.commands.create import create
from apijet.commands.remove import remove
import os


def test_create_projet():
    assert create('test_project', 1234, '127.0.0,1', './') is True


def test_get_info_project():
    os.chdir('./test_project')
    from test_project.test_project.project import info
    assert info['port'] == 1234
    assert info['name'] == 'test_project'


# def test_run_projet():


def test_remove_project():
    os.chdir('..')
    assert remove('./test_project') is True
