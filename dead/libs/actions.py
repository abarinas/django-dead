#!/usr/bin/env python

import subprocess


class DEADActions(object):
    def update_action(self):
        if self.parsed_args.update:
            subprocess.call([
                "pip",
                "install",
                "-U",
                self.dead_package
            ])
