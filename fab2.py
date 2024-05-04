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

    # Upload the archive using SCP
    put(archive_path, "/tmp/")
    
    return True
