#!/usr/bin/python3
""" fabric script to clean up versions """
import os
from fabric.api import *


env.user = 'ubuntu'
env.hosts = ['52.201.220.244', '54.221.180.200']


def do_clean(number=0):
    """ deletes out-of-date archives """
    if int(number) <= 1:
        number = 1
    else:
        number = int(number)

    # clean the local machine
    number_local = int(local("ls -1 versions | wc -l", capture=True))
    number_local_to_delete = number_local - number
    if number_local_to_delete > 0:
        first = "ls -1tr versions | head -n "
        second = " | xargs -I{} echo versions/{} | xargs rm"
        local("{} {} {}".format(first, number_local_to_delete, second))

    # clean the remote machine
    number_remote = int(run("ls -1 /data/web_static/releases | wc -l"))
    number_remote_to_delete = number_remote - number
    if number_remote_to_delete > 0:
        first = "ls -1tr /data/web_static/releases  | head -n "
        secnd = "| xargs -I{} echo /data/web_static/releases/{} | xargs rm -rf"
        run("{} {} {}".format(first, number_remote_to_delete, secnd))
