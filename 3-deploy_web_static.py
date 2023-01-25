#!/usr/bin/python3
""" Fabric file to compress a folder """
from fabric.api import *
from datetime import datetime
import os

env.user = "ubuntu"
env.hosts = ['54.221.180.200', '52.201.220.244']


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


def do_deploy(archive_path):
    """ deploys """
    try:
        if not os.path.exists(archive_path):
            return False
        put(archive_path, '/tmp/')
        archive_name = archive_path.split('/')[-1]
        up_folder = '/data/web_static/releases/{}/'.format(archive_name[:-4])
        run('mkdir -p {}'.format(up_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_name, up_folder))
        run('rm /tmp/{}'.format(archive_name))
        run('mv {}web_static/* {}'.format(up_folder, up_folder))
        run('rm -rf {}web_static'.format(up_folder))
        run('rm -rf /data/web_static/current')
        run('ln -sf {} /data/web_static/current'.format(up_folder))
        print("New version deployed!")
        return True
    except Exception as e:
        return False


def deploy():
    """ compress and deploy web static """
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)
