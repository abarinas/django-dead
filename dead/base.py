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

        # Install pip dependencies
        self.install_pip_dependencies_definition()

        # Create new django project
        self.create_definition()

        # Run migration
        self.migration_definition()

        # Create system users
        self.system_users_definition()

        # Run server
        self.run_definition()

        # Template
        self.template_definition()

        # Bower
        self.bower_definition()

    def make_actions(self):
        # Update package
        self.update_action()

        # Delete project if exists
        self.delete_action()

        # Install operating system dependencies
        self.install_os_dependencies_action()

        # Install pip dependencies
        self.install_pip_dependencies_action()

        # Create new django project
        self.create_action()

        # Run migration
        self.migration_action()

        # Create system users
        self.system_users_action()

        # Run server
        self.run_action()

        # Template
        self.template_action()

        # Bower
        self.bower_action()

    def parse(self):
        self.make_definitions()
        self.parse_args()
        self.make_actions()
