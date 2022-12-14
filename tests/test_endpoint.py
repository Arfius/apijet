from apijet.commands.endpoint import add
from apijet.commands.endpoint import add_parser
from apijet.commands.endpoint import remove as remove_endpoint
from apijet.commands.create import create
from apijet.utils.opfile import load_project_file
from apijet.utils.opfile import remove_project
import argparse


def test_parser():
    parser = argparse.ArgumentParser(description='Testing apijet perser')
    sub_parsers = parser.add_subparsers(title="Actions")
    add_parser(sub_parsers)
    name_space = parser.parse_args(['endpoint', '--add', 'test_endpoint'])
    assert name_space.add == 'test_endpoint'
    assert name_space.database is False


def test_add_endpoint_database():
    assert create('test_project', 5083, '127.0.0.1', './') is True
    assert add('test_endpoint', './test_project', True) is True


def test_add_endpoint_no_database():
    assert add('test_endpoint_no_db', './test_project', False) is True


def test_file_projetc_updated():
    file_project = load_project_file('./test_project/apijet.json')
    assert 'test_endpoint' in file_project['endpoints']
    assert 'test_endpoint_no_db' in file_project['endpoints']
    assert len(file_project['endpoints']) == 2


def test_remove_endpoint():
    assert remove_endpoint('test_endpoint', './test_project') is True
    assert remove_project('./test_project') is True
