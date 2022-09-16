from apijet.commands.endpoint import add
from apijet.commands.endpoint import add_parser
from apijet.utils.opfile import remove_project
from apijet.commands.create import create
import argparse


def test_parser():
    parser = argparse.ArgumentParser(description='Testing apiJet perser')
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


def test_remove():
    assert remove_project('./test_project') is True
