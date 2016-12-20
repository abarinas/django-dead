#!/usr/bin/env python

import os


class Skeleton(object):
    def __init__(self, skeleton_repo, instance_dir, slug, short_title, long_title, domain, email, password, email_bcc_recipient):
        self.skeleton_repo = skeleton_repo
        self.instance_dir = instance_dir
        self.slug = slug
        self.short_title = short_title
        self.long_title = long_title
        self.domain = domain
        self.email = email
        self.password = password
        self.email_bcc_recipient = email_bcc_recipient

    def inject(self):
        self.export_repo()

    def export_repo(self):
        cmd = "svn export {}/trunk/".format(
            self.skeleton_repo
        )
        os.system(cmd)

        cmd = "mv -f trunk/* ."
        os.system(cmd)

        cmd = "mv -f trunk/.* ."
        os.system(cmd)

        cmd = "rm -Rf trunk"
        os.system(cmd)

    def adjust_settings(self):
        cmd = "mv conf.orig/* conf && rm -Rf conf.orig"
        os.system(cmd)

        # add custom_settings call in settings.py
        settings = os.path.join(
            self.instance_dir,
            "conf",
            "settings.py"
        )

        f = open(settings, "r")
        contents = f.read()
        f.close()

        contents += """
try:
    execfile(os.path.join(BASE_DIR, 'conf', 'custom_settings.py'))
except IOError:
    pass"""

        f = open(settings, "w")
        f.write(contents)
        f.close()

        settings = os.path.join(
            self.instance_dir,
            "conf",
            "custom_settings.py"
        )

        f = open(settings, "r")
        contents = f.read()
        f.close()

        contents = contents.replace("SLUG_PLACEHOLDER", self.slug)
        contents = contents.replace("SHORT_TITLE_PLACEHOLDER", self.short_title)
        contents = contents.replace("LONG_TITLE_PLACEHOLDER", self.long_title)
        contents = contents.replace("DOMAIN_PLACEHOLDER", self.domain)
        contents = contents.replace("EMAIL_USER_PLACEHOLDER", self.email)
        contents = contents.replace("EMAIL_PASSWORD_PLACEHOLDER", self.password)
        contents = contents.replace("EMAIL_BCC_RECIPIENT_PLACEHOLDER", self.email_bcc_recipient)

        f = open(settings, "w")
        f.write(contents)
        f.close()

