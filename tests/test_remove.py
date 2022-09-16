from apijet.commands.create import create
from apijet.commands.remove import remove
from apijet.commands.remove import add_parser
import argparse


def test_parser():
    parser = argparse.ArgumentParser(description='Testing apiJet perser')
    sub_parsers = parser.add_subparsers(title="Actions")
    add_parser(sub_parsers)
    name_space = parser.parse_args(['remove', '--name', 'test_project'])
    assert name_space.name == 'test_project'


def test_remove_project():
    assert create('test_project', 5083, '127.0.0.1', './') is True
    assert remove('./test_project') is True


def test_remove_project_wrong_folder():
    assert remove('./') is False
