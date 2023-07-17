#!/usr/bin/python3

"""import for fabric to compress a folder"""
from fabric.api import *


def do_pack():
    local("mkdir -p versions")
    path = "/home/konadulordkweku/AirBnB_clone/web_static"
    with lcd("versions"):
        local(f"tar -cavf web_static_2023071445.tgz {path}")
        return None


if __name__ == "__main__":
    do_pack()
