#!/usr/bin/env python

import subprocess
import os


class DEADActions(object):
    def update_action(self):
        if self.parsed_args.update:
            subprocess.call([
                "pip",
                "install",
                "-U",
                self.dead_package
            ])

    def delete_action(self):
        if self.parsed_args.delete:
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
