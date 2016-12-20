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

    # handler class
    dead_commander = DEADCommander(
        parser=parser
    )

    dead_commander.parse()

if __name__ == "__main__":
    main()