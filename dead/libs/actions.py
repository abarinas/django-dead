#!/usr/bin/env python

import subprocess
import os

from skeleton import Skeleton


class DEADActions(object):
    def update_action(self, jump=False):
        if not self.parsed_args.update and not jump:
            return

        subprocess.call([
            "pip",
            "install",
            "-U",
            self.dead_package
        ])

    def delete_action(self, jump=False):
        if not self.parsed_args.delete and not jump:
            return

        to_ignore = [
            ".git",
            ".gitignore",
        ]

        for item in os.listdir(self.instance_dir):
            if item in to_ignore:
                continue

            subprocess.call([
                "rm",
                "-Rf",
                item,
            ])

    def install_os_dependencies_action(self, jump=False):
        if not self.parsed_args.osdependencies and not jump:
            return

        cmd = "sh {}".format(
            self.os_dependencies_file
        )

        os.system(cmd)

    def install_pip_dependencies_action(self, jump=False):
        if not self.parsed_args.pip and not jump:
            return

        for pip_file in self.pip_files:
            os.system("pip install -U -r {}".format(
                pip_file
            ))

    def create_action(self, jump=False):
        if not self.parsed_args.create and not jump:
            return

        os.system("django-admin.py startproject conf {}".format(
            self.instance_dir
        ))

    def migration_action(self, jump=False):
        if not self.parsed_args.migration and not jump:
            return

        os.system("python manage.py makemigrations")
        os.system("python manage.py migrate")

    def run_action(self, jump=False):
        if not self.parsed_args.live and not jump:
            return

        os.system("python manage.py runserver 0.0.0.0:{}".format(
            self.running_port
        ))

    def system_users_action(self, jump=False):
        if not self.parsed_args.systemusers and not jump:
            return

        fixtures_dir = self.fixtures_dir
        dead_users_json = os.path.join(fixtures_dir, "dead_users.json")
        os.system("python manage.py loaddata {}".format(
            dead_users_json
        ))

    def template_action(self, jump=False):
        if not self.parsed_args.template and not jump:
            return

        if not jump:
            template_name, slug, short_title, long_title, domain, email, password, email_bcc_recipient = self.parsed_args.template
        else:
            template_name, slug, short_title, long_title, domain, email, password, email_bcc_recipient = [
                "basic",
                "dead",
                "DEAD",
                "DEAD Project",
                "dead.000cortazar000.pes",
                "dead@000cortazar000.pes",
                "12345",
                "info@000cortazar000.pes"
            ]

        # Inject skeleton to instance
        skeleton = Skeleton(
            skeleton_repo=self.skeleton_package,
            instance_dir=self.instance_dir,
            slug=slug,
            short_title=short_title,
            long_title=long_title,
            domain=domain,
            email=email,
            password=password,
            email_bcc_recipient=email_bcc_recipient
        )
        skeleton.inject()

    def bower_action(self, jump=False):
        if not self.parsed_args.bower and not jump:
            return

        os.system("cd {} && bower update --save --allow-root".format(
            self.instance_dir
        ))

    def asap_action(self, jump=False):
        if not self.parsed_args.asap and not jump:
            return

        self.update_action(jump=True)
        self.install_os_dependencies_action(jump=True)
        self.delete_action(jump=True)
        self.create_action(jump=True)
        self.migration_action(jump=True)
        self.system_users_action(jump=True)
        self.template_action(jump=True)
        self.install_pip_dependencies_action(jump=True)
        self.migration_action(jump=True)
        self.bower_action(jump=True)
