import argparse
from apijet.commands.create import add_parser as add_parser_create
from apijet.commands.create import create
from apijet.commands.endpoint import add_parser as add_parser_endpoint
from apijet.commands.endpoint import add
from apijet.commands.endpoint import remove as remove_endopoint
from apijet.commands.remove import remove
from apijet.commands.remove import add_parser as add_parser_remove
from apijet.version import __version__
import os
import sys

parser = argparse.ArgumentParser(description=f' - Api Generator v: {__version__}')
sub_parsers = parser.add_subparsers(title="Actions")
add_parser_create(sub_parsers)
add_parser_endpoint(sub_parsers)
add_parser_remove(sub_parsers)
current_path = os.getcwd()


def main():
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    args = parser.parse_args()
    if args.action == 'create':
        create(args.name, args.port, args.address, current_path)
    elif args.action == 'endpoint':
        if args.add:
            add(args.add, current_path,  args.database)
        elif args.remove:
            print("ℹ️ > Are you sure you want to delete the endpoint?")
            answer = input("[y/N]")
            if answer.lower() == 'y':
                remove_endopoint(args.remove, current_path)
    elif args.action == 'remove':
        print("ℹ️ > Are you sure you want to delete the project?")
        answer = input("[y/N]")
        if answer.lower() == 'y':
            remove(current_path)
