#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
from datetime import datetime
from fabric.api import local


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
