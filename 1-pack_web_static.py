#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    today_date = datetime.utcnow()
    date = f"{today_date.year}{today_date.month}{today_date.day}"
    time = f"{today_date.hour}{today_date.minute}{today_date.second}"
    archive_name = f"versions/web_static_{date}{time}.tgz"
    local("mkdir -p versions")
    try:
        local(f"tar -cvzf {archive_name} web_static")
        return archive_name
    except Exception:
        return None
