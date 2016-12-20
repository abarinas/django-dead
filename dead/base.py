#!/usr/bin/env python

from libs.actions import DEADActions
from libs.common import DEADCommon
from libs.definitions import DEADDefinition


class DEADCommander(DEADActions, DEADDefinition, DEADCommon):
    def make_definitions(self):
        # Update package
        self.update_definition()

        # Delete project if exists
        self.delete_definition()

        # Install operating system dependencies
        self.install_os_dependencies_definition()

    def make_actions(self):
        # Update package
        self.update_action()

        # Delete project if exists
        self.delete_action()

        # Install operating system dependencies
        self.install_os_dependencies_action()

    def parse(self):
        self.make_definitions()
        self.parse_args()
        self.make_actions()
