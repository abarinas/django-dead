#!/usr/bin/env python

import os


class DEADCommon(object):
    def __init__(self, parser):
        self.parsed_args = None
        self.dead_package = "git+https://github.com/000paradox000/django-dead.git"
        self.skeleton_package = "git+https://github.com/000paradox000/django-dead-skeleton.git"
        self.running_port = "9500"
        self.parser = parser

    def parse_args(self):
        self.parsed_args = self.parser.parse_args()

    @property
    def instance_dir(self):
        return os.getcwd()

    @property
    def package_dir(self):
        return os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

    @property
    def assets_dir(self):
        return os.path.join(
            self.package_dir,
            "assets"
        )

    @property
    def fixtures_dir(self):
        return os.path.join(
            self.assets_dir,
            "fixtures"
        )

    @property
    def os_dependencies_file(self):
        return os.path.join(
            self.assets_dir,
            "dependencies",
            "os.sh"
        )

    @property
    def apache_dir(self):
        return os.path.join(
            self.assets_dir,
            "apache"
        )

    @property
    def pip_files(self):
        out = [
            os.path.join(
                self.assets_dir,
                "dependencies",
                "pip.txt"
            ),
        ]

        return out
