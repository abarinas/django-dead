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

    # group parser
    group = parser.add_mutually_exclusive_group()

    # handler class
    dead_commander = DEADCommander(
        parser=parser,
        group=group
    )

    dead_commander.parse()

if __name__ == "__main__":
    main()