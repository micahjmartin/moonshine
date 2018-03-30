import sys
import yaml
from . import CONFIG, debug
from subprocess import Popen, PIPE


def execute(args, stdout=sys.stdout, stderr=sys.stderr, stdin=None):
    '''
    Execute a command. Pass the args as an array if there is more than one
    '''
    debug(args)
    try:
        proc = Popen(args, stdin=stdin, stdout=stdout, stderr=stderr)
        proc.communicate()
        return proc.wait()
    except Exception as E:
        debug(E)
        return 255


def delInterface(ip):
    '''
    delete a virtual interface with the specified IP address
    '''
    return execute(("ip", "addr", "del", "{}/32".format(ip), "dev",
            CONFIG.get("interface", "eth0")))


def addInterface(ip):
    '''
    add a virtual interface with the specified IP address
    '''
    return execute(("ip", "addr", "add", "{}/24".format(ip), "brd", "+", "dev",
            CONFIG.get("interface", "eth0:")))


def addRoute(ip):
    '''
    '''
    pass
