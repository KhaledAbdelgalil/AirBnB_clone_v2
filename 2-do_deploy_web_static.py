#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
from datetime import datetime
from fabric.api import *
from os import path
env.user = 'ubuntu'
env.hosts = ['54.237.48.43', '35.175.132.199']


def do_deploy(archive_path):
    """Create a tar gzipped archive of the directory web_static."""
    if path.exists(archive_path) is False:
        return False
    put(archive_path, "/tmp/")
    filename: str = path.basename(archive_path, )
    filename_without_extension = filename.split(".")[0]

    ''' create required folder and uncompress'''
    if run(f"mkdir -p /data/web_static/releases/\
           {filename_without_extension}").failed:
        return False

    if run(f"rm -rf /data/web_static/releases/\
           {filename_without_extension}/*").failed:
        return False

    if run(f"tar -xzf /tmp/{filename} -C /data/web_static/releases/\
           {filename_without_extension}").failed:
        return False

    ''' Copy the data from web_static folder to parent folder '''
    if run(f"mv -uf /data/web_static/releases/\
           {filename_without_extension}/web_static/* \
            /data/web_static/releases/\
            {filename_without_extension}").failed:
        return False

    if run(f"rm -dr /data/web_static/releases/\
           {filename_without_extension}/web_static/").failed:
        return False

    # Delete the archive
    if run(f"rm /tmp/{filename}").failed:
        return False

    ''' Delete the symbolic link to '/data/web_static/current' and
    link it to the newly uncompressed folder'''
    if run(f'rm -rf /data/web_static/current').failed:
        return False

    if run(f'ln -s /data/web_static/releases/\
           {filename_without_extension} /data/web_static/current').failed:
        return False

    return True
