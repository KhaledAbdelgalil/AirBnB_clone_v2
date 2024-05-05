#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """


from fabric.api import run, put, env
from os.path import exists
env.hosts = ['54.237.48.43', '35.175.132.199']


def do_deploy(archive_path):
    """ A function that distributes an archive to your web servers """
    try:
        if exists(archive_path):
            file_name = archive_path.split("/")[-1]
            file_ext = file_name.split(".")[0]
            file_no_ext = "web_static"
            path = "/data/web_static/releases/"
            put(archive_path, '/tmp/')
            run('mkdir -p {}{}/'.format(path, file_ext))
            run('tar -xzf /tmp/{} -C {}{}/'.format(file_name,
                                                   path, file_ext))
            run('rm /tmp/{}'.format(file_name))
            run('mv {0}{1}/{2}/* {0}{1}/'.format(path, file_ext, file_no_ext))
            run('rm -rf /data/web_static/current')
            run('ln -s {}{}/ /data/web_static/current'.format(path, file_ext))
            return True
        else:
            return False
    except Exception:
        return False
