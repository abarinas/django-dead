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
            nvars=8,
            type=str
        )
        #
        # self.subparser.add_argument(
        #     "--templatename",
        #     type=str,
        #     help="Template name",
        #     default="basic"
        # )
        #
        # self.subparser.add_argument(
        #     "--slug",
        #     type=str,
        #     help="slug name for the project. This is used for naming many items like the static_url, media_url, etc",
        #     default="dead"
        # )
        #
        # self.subparser.add_argument(
        #     "--shorttitle",
        #     type=str,
        #     help="used by the basic template in the navbar brand place",
        #     default="DEAD"
        # )
        #
        # self.subparser.add_argument(
        #     "--longtitle",
        #     type=str,
        #     help="used by the basic template in the navbar brand place",
        #     default="DEAD Project"
        # )
        #
        # self.subparser.add_argument(
        #     "--domain",
        #     type=str,
        #     help="http domain used by the project when running in production",
        #     default="dead.000cortazar000.pes"
        # )
        #
        # self.subparser.add_argument(
        #     "--email",
        #     type=str,
        #     help="email account used by the project for sending messages",
        #     default="dead@000paradox000.pes"
        # )
        #
        # self.subparser.add_argument(
        #     "--password",
        #     type=str,
        #     help="email account password",
        #     default="12345"
        # )
        #
        # self.subparser.add_argument(
        #     "--emailbccrecipient",
        #     type=str,
        #     help="main bcc recipient of the messages sent by the project",
        #     default="info@000cortazar000.pes"
        # )
        #
