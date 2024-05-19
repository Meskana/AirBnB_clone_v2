#!/usr/bin/env bash
"""
a Fabric script that generates a .tgz archive from the contents of the web_staticf
older of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import *
from datetime import datetime
from os.path import isdir
import os


def do_pack():


    """ A sceript that generates a .tgz archive"""

    try:
        if isdir('versions') is false:
            local('sudo mkdir -p versions')
        now = datetime.now()
        t_now = now.strftime('%Y%m%d%H%M%S')
        local(f'sudo tar -cvzf versions/web_static_{t_now}.tgz web_static')
        f_path = f'versions/web_static_{t_now}.tgz'
        f_size = os.path.getsize(f_path)
        print(f'web_static packed: versions/web_static_{t_now}.tgz -> {f_size}Bytes')
        return f_path
    except:
        return None
