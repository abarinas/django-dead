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

    # template subparser
    subparser = subparsers.add_parser(
        'add_template',
        help='Create a new template based django project (DEAD project)'
    )

    # handler class
    dead_commander = DEADCommander(
        parser=parser,
        subparser=subparser
    )

    dead_commander.parse()

if __name__ == "__main__":
    main()