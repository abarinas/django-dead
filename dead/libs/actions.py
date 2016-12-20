#!/usr/bin/env python

import subprocess
import os

from skeleton import Skeleton


class DEADActions(object):
    def update_action(self):
        if not self.parsed_args.update:
            return

        subprocess.call([
            "pip",
            "install",
            "-U",
            self.dead_package
        ])

    def delete_action(self):
        if not self.parsed_args.delete:
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

    def install_os_dependencies_action(self):
        if not self.parsed_args.osdependencies:
            return

        cmd = "sh {}".format(
            self.os_dependencies_file
        )

        os.system(cmd)

    def install_pip_dependencies_action(self):
        if not self.parsed_args.pip:
            return

        for pip_file in self.pip_files:
            os.system("pip install -U -r {}".format(
                pip_file
            ))

    def create_action(self):
        if not self.parsed_args.create:
            return

        os.system("django-admin.py startproject conf {}".format(
            self.instance_dir
        ))

    def migration_action(self):
        if not self.parsed_args.migration:
            return

        os.system("python manage.py makemigrations")
        os.system("python manage.py migrate")

    def run_action(self):
        if not self.parsed_args.live:
            return

        os.system("python manage.py runserver 0.0.0.0:{}".format(
            self.running_port
        ))

    def system_users_action(self):
        if not self.parsed_args.systemusers:
            return

        fixtures_dir = self.fixtures_dir
        dead_users_json = os.path.join(fixtures_dir, "dead_users.json")
        os.system("python manage.py loaddata {}".format(
            dead_users_json
        ))

    def template_action(self):
        if not self.parsed_args.template:
            return

        template_name, slug, short_title, long_title, domain, email, password, email_bcc_recipient = self.parsed_args.template

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