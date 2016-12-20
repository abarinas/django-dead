#!/usr/bin/env python

import argparse
import sys

from dead import DEADCommander


def set_default_subparser(self, name, args=None):
    """default subparser selection. Call after setup, just before parse_args()
    name: is the name of the subparser to call by default
    args: if set is the argument list handed to parse_args()

    , tested with 2.7, 3.2, 3.3, 3.4
    it works with 2.6 assuming argparse is installed
    """
    subparser_found = False
    for arg in sys.argv[1:]:
        if arg in ['-h', '--help']:  # global help if no subparser
            break
    else:
        for x in self._subparsers._actions:
            if not isinstance(x, argparse._SubParsersAction):
                continue
            for sp_name in x._name_parser_map.keys():
                if sp_name in sys.argv[1:]:
                    subparser_found = True
        if not subparser_found:
            # insert default in first position, this implies no
            # global options without a sub_parsers specified
            if args is None:
                sys.argv.insert(1, name)
            else:
                args.insert(0, name)

argparse.ArgumentParser.set_default_subparser = set_default_subparser


def main():
    """ Command line interface
    """
    # argument parser
    parser = argparse.ArgumentParser(
        "DEAD command line interface"
    )

    # subparsers
    subparsers = parser.add_subparsers()

    # add template parser
    add_template_parser = subparsers.add_parser(
        'add_template',
        help='Create a new template based django project (DEAD project)'
    )

    # handler class
    dead_commander = DEADCommander(
        parser=parser,
        subparser=add_template_parser
    )

    dead_commander.parse()

if __name__ == "__main__":
    main()