import sys, os, string
if string.find(os.path.abspath(sys.argv[0]), os.sep+'Twisted') != -1:
    sys.path.insert(0, os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]), os.pardir, os.pardir)))
if hasattr(os, "getuid") and os.getuid() != 0:
    sys.path.insert(0, os.path.abspath(os.getcwd()))
### end of preamble

import os
from os.path import dirname, join
from collective.transcode import daemon
from twisted.scripts.twistd import run
from twisted.python import log

cmd_map = dict(
    fg=('-n',),
    start = (),
)

def main(args):
    if args[1] == 'stop':
        try:
            pid = int(file('%s/transcodedaemon.pid' % args[0]).read())
            os.kill(pid, 15)
            print "TranscodeDaemon stopped"
        except:
            print "TranscodeDaemon not running"
        return
    os.environ['TRANSCODEDAEMON_ROOT'] = args[0]
    py_file = join(dirname(daemon.__file__), 'transcodedaemon.py')
    if '--pidfile' in args:
        pidfile = args[args.index('--pidfile')+1]
    else:
        pidfile = '%s/transcodedaemon.pid' % args[0]
    logfile = '%s/transcodedaemon.log'  % args[0]
    options = ['-y', py_file, '--pidfile', pidfile, '--logfile', logfile]


    options.extend(cmd_map[args[1]])
    sys.argv[1:]=[]
    sys.argv.extend(options)
    run()
