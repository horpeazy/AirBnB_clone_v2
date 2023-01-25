#!/usr/bin/python3
""" Fabric file to compress a folder """
from fabric.api import *
from datetime import datetime
import os

env.user = "ubuntu"
env.hosts = ['54.221.180.200', '52.201.220.244']


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
