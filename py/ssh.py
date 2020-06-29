from __future__ import print_function

import paramiko
from hosts import *
import sys,os
from main import *

def connect(site,clock='',command="/usr/bin/service"):
    if clock == '':
        for item in hosts[site]:
            print(hosts[site][item]['host'])
            host = hosts[site][item]['host']
            password = hosts[site][item]['pass']
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.get_host_keys()
            client.connect(host, username='root', password=password)
            stdin, stdout, stderr = client.exec_command(command)
            print(str(stdout.read(),encoding='ascii'))
            client.close()
    else:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.load_system_host_keys()
        client.get_host_keys()
        client.connect(hosts[site][clock]['host'], username='root', password=hosts[site][clock]['pass'])
        stdin, stdout, stderr = client.exec_command(command)
        print(str(stdout.read(),encoding='ascii'))
        client.close()
