from subprocess import Popen, PIPE
from . import debug


def execute(args):
    '''
    Execute a command. Pass the args as an array if there is more than one
    '''
    debug("Executing: {}".format(args))
    retval = {'status': 255}
    try:
        proc = Popen(args, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE,
                     close_fds=True)
        retval['stdout'] = proc.stdout.read().decode("utf-8")
        retval['stderr'] = proc.stderr.read().decode("utf-8")
        retval['status'] = proc.wait()
    except Exception as E:
        debug(args)
        debug(E)
    return retval


