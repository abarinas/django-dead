#!/usr/bin/env python


class DEADDefinition(object):
    def update_definition(self):
        self.parser.add_argument(
            "-u",
            "--update",
            help="Update DEAD package",
            action="store_true"
        )

    def delete_definition(self):
        self.parser.add_argument(
            "-d",
            "--delete",
            help="Delete project",
            action="store_true"
        )

    def install_os_dependencies_definition(self):
        self.parser.add_argument(
            "-s",
            "--osdependencies",
            help="Install Operating System dependencies",
            action="store_true"
        )
