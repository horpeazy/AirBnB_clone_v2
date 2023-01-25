#!/usr/bin/python3
""" Fabric file to compress a folder """
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ compress a folder """
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        directory = "versions/web_static_{}.tgz".\
            format(datetime.now().strftime("%Y%m%d%H%M%S"))
        local('tar -cvzf {} web_static'.format(directory))
        return directory
    except Exception:
        return None
