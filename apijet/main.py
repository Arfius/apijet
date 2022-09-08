import argparse
from apijet.commands.create import add_parser
from apijet.commands.create import create
from version import __version__
import pathlib

parser = argparse.ArgumentParser(description=f'apiJet - Api Generator v: {__version__}')
sub_parsers = parser.add_subparsers(title="Actions")
add_parser(sub_parsers)

current_path = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)

    if args.action == 'create':
        create(args.name, args.port, current_path)
