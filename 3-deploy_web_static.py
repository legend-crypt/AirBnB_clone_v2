#!/usr/bin/python3
"""script that creates and
distributes an archive to your web servers"""
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """script that creates and
    distributes an archive to your web servers"""
    archive_path = do_pack()
    print(f"archive_path {archive_path}")
    if archive_path is False:
        return False
    deployed = do_deploy(archive_path)
    print(f"deployed {deployed}")
    return deployed
