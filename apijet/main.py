import argparse
from apijet.commands.create import add_parser as add_parser_create
from apijet.commands.create import create
from apijet.commands.endpoint import add_parser as add_parser_endpoint
from apijet.commands.endpoint import add
from apijet.version import __version__
import os

parser = argparse.ArgumentParser(description=f'apiJet - Api Generator v: {__version__}')
sub_parsers = parser.add_subparsers(title="Actions")
add_parser_create(sub_parsers)
add_parser_endpoint(sub_parsers)
current_path = os.getcwd()


def main():
    args = parser.parse_args()
    if args.action == 'create':
        create(args.name, args.port, args.address, current_path)
    elif args.action == 'endpoint':
        if args.add:
            add(args.add, current_path)
