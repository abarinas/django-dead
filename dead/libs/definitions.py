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

    def install_pip_dependencies_definition(self):
        self.parser.add_argument(
            "-p",
            "--pip",
            help="Install pip dependencies",
            action="store_true"
        )

    def create_definition(self):
        self.parser.add_argument(
            "-c",
            "--create",
            help="Create new django project",
            action="store_true"
        )

    def migration_definition(self):
        self.parser.add_argument(
            "-m",
            "--migration",
            help="Run makemigrations and migration",
            action="store_true"
        )

    def run_definition(self):
        self.parser.add_argument(
            "-l",
            "--live",
            # help="Run server on 0.0.0.0:{}".format(self.running_port),
            help="Run server",
            action="store_true"
        )
