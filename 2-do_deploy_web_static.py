#!/usr/bin/python3
""" Fabric file to compress a folder """
from fabric.api import run, put, env
from datetime import datetime
import os

env.user = "ubuntu"
env.hosts = ['52.201.220.244', '54.221.180.200']

def do_deploy(archive_path):
    try:
        if not os.path.exists(archive_path):
            return False
        put(archive_path, '/tmp/')
        archive_name = archive_path.split('/')[-1]
        upload_folder = '/data/web_static/releases/{}'.format(archive_name[:-3])
        run('tar -xzf /tmp/{} -C {}'.format(archive_name, upload_folder))
        run('rm /tmp/{}'.format(archive_name))
        run('ln -sf /data/web_static/releases/{} /data/web_static/current'.format(archive_name[:-3]))
        return True
    except Exception:
        return False
