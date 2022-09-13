#!/usr/bin/python3
"""
Compress before sending
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """return the archive path if the archive has been correctly generated.
    Otherwise, it should return None
    """
    local("mkdir -p versions")
    date = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    file = local("tar -cvzf versions/web_static_{}.tgz web_static"
                 .format(datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')))
    if file.failed:
        return None
    return ("versions/web_static_{}.tgz".format(date))
