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
    try:
        if exists(archive_path):
            file_name = archive_path.split("/")[-1]
            file_no_ext = file_name.split(".")[0]
            path = "/data/web_static/releases/"
            put(archive_path, '/tmp/')
            run('mkdir -p {}{}/'.format(path, file_no_ext))
            run('tar -xzf /tmp/{} -C {}{}/'.format(file_name,
                                                   path, file_no_ext))
            run('rm /tmp/{}'.format(file_name))
            run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_no_ext))
            run('rm -rf {}{}/web_static'.format(path, file_no_ext))
            run('rm -rf /data/web_static/current')
            run('ln -s {}{}/ /data/web_static/current'.format(
                path, file_no_ext))
            return True
        else:
            return False
    except Exception:
        return False


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
