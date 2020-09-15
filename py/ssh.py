from __future__ import print_function

import paramiko
from hosts import *
import sys,os
from main import *

def get_creds(site,clock=''):
    if clock == '':
        for item in hosts[site]:
            host = hosts[site][item]['host']
            password = hosts[site][item]['pass']
            name = connect(site,item,'uname -a')
            cred_print(host,password,name)
    else:
        host = hosts[site][clock]['host']
        password = hosts[site][clock]['pass']
        name = connect(site,clock,'uname -a')
        cred_print(host,password,name)

def connect(site,clock='',command="/usr/bin/service"):
    # print(clock)
    # print(hosts[site][clock]['host'])
    # print(hosts[site][clock]['pass'])

    if clock == '':
        for item in hosts[site]:
            print(hosts[site][item]['host'])
            host = hosts[site][item]['host']
            password = hosts[site][item]['pass']
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.get_host_keys()
            try:
                client.connect(host, username='root', password=password)
                stdin, stdout, stderr = client.exec_command(command)
                print(str(stdout.read(),encoding='ascii'))
                client.close()
            except Exception as e:
                exception_handle(clock,host,password)

    else:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.load_system_host_keys()
        client.get_host_keys()
        try:
            client.connect(hosts[site][clock]['host'], username='root', password=hosts[site][clock]['pass'])
            stdin, stdout, stderr = client.exec_command(command)
            print(str(stdout.read(),encoding='ascii'))
            client.close()
        except Exception as e:
            exception_handle(clock,hosts[site][clock]['host'],hosts[site][clock]['pass'])



def exception_handle(clock,host,password):

    print("----------------ERROR-------------------")
    print("SSH can't reach the host")
    print("Telnet to the host and check SSH service")
    print("Example: telnet "+host+" ; user - root ; password - "+password+" ; service ssh on")
    print("Or report to you administrator")
    print("----------------------------------------")

def cred_print(host,password,info):
    print('-----------------------------')
    print('Host '+host+' password is: '+password)
    print('Host info: ')
