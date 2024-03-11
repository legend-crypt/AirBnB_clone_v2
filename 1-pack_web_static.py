#!/usr/bin/env python3
"""script that generates a
.tgz archive from the contents
of the web_static
folder"""

from fabric.api import local, settings, cd
from datetime import datetime


def do_pack():
    """script that generates a
    .tgz archive from the
    contents of the web_static
    folder"""
    file_name = "web_static_{}".format(
        datetime.now().strftime('%Y%m%d%H%M%S')
    )
    with settings(warn_only=True):
        directory = "versions"
        local(f"mkdir -p {directory}")
    archive_path = "{}/{}".format(directory, file_name)
    archive_command = local(f"tar -cvzf {archive_path}.tgz ./web_static")
    if archive_command.succeeded:
        return f"{archive_path}.tgz"
    else:
        return None
