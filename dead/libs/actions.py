#!/usr/bin/env python

import subprocess
import os


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
        if not self.parsed_args.migrate:
            return

        os.system("python manage.py makemigrations")
        os.system("python manage.py migrate")
