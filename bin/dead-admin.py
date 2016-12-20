#!/usr/bin/env python

import argparse

from dead import DEADCommander


def main():
    """ Command line interface
    """
    # argument parser
    parser = argparse.ArgumentParser(
        "DEAD command line interface"
    )

    # subparsers
    subparsers = parser.add_subparsers()

    # default
    default_parser = subparsers.add_parser()

    # add template parser
    add_template_parser = subparsers.add_parser(
        'add_template',
        help='Create a new template based django project (DEAD project)'
    )

    # handler class
    dead_commander = DEADCommander(
        parser=default_parser,
        subparser=add_template_parser
    )

    dead_commander.parse()

if __name__ == "__main__":
    main()