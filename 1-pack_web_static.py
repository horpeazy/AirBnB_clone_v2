#!/usr/bin/python3
""" Fabric file to compress a folder """
from fabric.api import local
from datetime import datetime

def do_pack():
    """ compress a folder """
    local('mkdir versions')
    directory = "versions/web_static_{}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))
    result = local('tar -cvzf {} web_static'.format(directory))
    if result.succeeded:
        return directory
    return None
