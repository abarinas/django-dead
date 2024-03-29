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
            "-o",
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
            help="Run server on 0.0.0.0:{}".format(self.running_port),
            action="store_true"
        )

    def system_users_definition(self):
        self.parser.add_argument(
            "-s",
            "--systemusers",
            help="Create system users",
            action="store_true"
        )

    def template_definition(self):
        self.parser.add_argument(
            "-t",
            "--template",
            help="Create a new template based django project (DEAD project)",
            nargs=8,
            type=str
        )

    def bower_definition(self):
        self.parser.add_argument(
            "-b",
            "--bower",
            help="Update bower dependencies",
            action="store_true"
        )

    def asap_definition(self):
        self.parser.add_argument(
            "-a",
            "--asap",
            help="Generate a project ASAP",
            action="store_true"
        )

    def notify_definition(self):
        self.parser.add_argument(
            "-n",
            "--notify",
            help="Send desktop notification (notify-send) when executed",
            action="store_true"
        )
