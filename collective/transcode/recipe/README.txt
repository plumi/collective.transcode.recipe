collective.transcode.recipe
============

Introduction
============
buildout recipe that sets collective.transcode.daemon. collective.transcode.daemon is a fork of atreal's darksnow.convertdaemon (https://svn.atreal.net/public/svn.darksnow.org/ConvertDaemon) featuring improvements, and a code cleanout. 


How to get it working
============

Needs ffmpeg. python-twisted and python-twisted-web2 are included on the buildout so no need to install seperately.
Tested on Linux (Ubuntu 9.04) and Mac OS X 10.5.7.


Try this
user@user:~$ svn co https://svn.plone.org/svn/collective/collective.transcode.recipe/trunk transcode.buildout
user@user:~$ cd transcode.buildout
user@user:~/transcode.buildout$ python2.4 bootstrap.py 
user@user:~/transcode.buildout$ ./bin/buildout -v
user@user:~/transcode.buildout$ ./bin/transcodedaemon fg

Initializing
...
2009-11-25 19:28:14+0200 [-] Scheduler thread running



Configuration options
============

On buildout.cfg, upon transcodedaemon section, the following settings can be configured:

listen_host=locahost #ip or hostname to listen
listen_port=8888     #port to use
videofolder=videos   #path of folder where transcoded videos are stored

 
==How can I change the quality and format of the transcoded files
You'll have to change the profiles list. On buildout.cfg, upon transcodedaemon section, edit the profiles ('low', 'high' are the defaults)


Todo
============
* Use xml conf to create video path
* Better video URL (path/origfile.avi/profileid/filename.flv)



