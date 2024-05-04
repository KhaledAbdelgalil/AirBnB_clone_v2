#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """


from fabric.api import *
from os import path
from datetime import datetime
env.hosts = ['54.237.48.43', '35.175.132.199']


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    today_date = datetime.today()
    date = f"{today_date.year}{today_date.month:02}{today_date.day:02}"
    time = f"{today_date.hour:02}{today_date.minute:02}{today_date.second:02}"
    archive_name = f"versions/web_static_{date}{time}.tgz"
    local("mkdir -p versions")
    try:
        local(f"tar -cvzf {archive_name} web_static")
        return archive_name
    except Exception:
        return None


def do_deploy(archive_path):
    """ A function that distributes an archive to your web servers """
    if path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
