#!/usr/bin/python3
"""script (based on the file 1-pack_web_static.py)
that distributes an archive to
your web servers"""
from fabric.api import run, put, env
from os import path


env.hosts = ["54.210.123.227", "100.26.172.200"]


def do_deploy(archive_path):
    """script (based on the file 1-pack_web_static.py) that
    distributes an archive
    to your web servers"""
    try:
        if path.exists(f"./{archive_path}") is False:
            return False
        timestamp = archive_path[20:-4]
        put(f"{archive_path}", "/tmp")
        run("mkdir -p /data/web_static/releases/web_static_{}".
            format(timestamp))
        run("tar -xzf /tmp/web_static_{}.tgz -C \
            /data/web_static/releases/web_static_{}".
            format(timestamp, timestamp))
        run("mv /data/web_static/releases/web_static_{}/web_static/* \
            /data/web_static/releases/web_static_{}/".
            format(timestamp, timestamp))
        run("rm -rf /data/web_static/releases/web_static_{}/web_static".
            format(timestamp))
        run("rm -rf /tmp/web_static_{}.tgz".
            format(timestamp))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/web_static_{}\
            /data/web_static/current".
            format(timestamp))
        return True
    except Exception as e:
        return False
