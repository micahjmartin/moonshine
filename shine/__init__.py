import yaml
import pty
import os
import json
import shlex

from .tools import execute

CONFIG = {}

def debug(*args, **kwargs):
    print(*args, **kwargs)


# Load the configuration file
try:
    with open("/etc/moonshine/moonshine.yml") as fil:
        CONFIG = yaml.load(fil)
except Exception as E:
    pass

# The main function to accept
def newProxy():
    '''
    Initialize a new proxy to connect to the remote box
    '''
    def badRemote(user):
        print("Pass the new connection information to moonshine. e.g.")
        print("ssh {}@moonshine root@remoteip".format(user))
        quit(1)

    i = {}
    i['user'] = os.environ['USER']
    i['ip'] = os.environ.get('SSH_CONNECTION', False)
    i['dest'] = os.environ.get('SSH_ORIGINAL_COMMAND',False)
    
    # Make sure we are in an ssh session
    if not i['ip'] :
        print("Moonshine must be run from within an SSH session!\nExiting...")
        quit(255)
    else:
        i['ip'] = i['ip'].split()[1]  # Get the actual IP from env var
    
    if i['dest'] is False:
        badRemote(i['user'])
    # Print context
    print(i)
    command = 'ssh -tt -A -o StrictHostKeyChecking=no {}'.format(i['dest'])
    print(command, flush=True)
    command = shlex.split(command)
    pty.spawn(command)
