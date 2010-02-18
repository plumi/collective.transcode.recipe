Introduction
============
buildout recipe for collective.transcode.daemon


Installation
------------

You can find a sample buildout here:
https://svn.plone.org/svn/collective/collective.transcode.buildout/trunk/

The transcoding scripts provided with the above buildout require ffmpeg and ffmpeg2theora.


$ svn co https://svn.plone.org/svn/collective/collective.transcode.buildout/trunk transcode.buildout
$ cd transcode.buildout
$ python bootstrap.py 
$ ./bin/buildout -v
$ ./bin/transcodedaemon fg
Initializing
...
2009-11-25 19:28:14+0200 [-] Scheduler thread running


Supported options
-----------------

The recipe supports the following options:

listen_host
	hostname to listen
listen_port
	port to use
videofolder
	relative path of folder where transcoded videos are stored
profiles
	a python list of dicts specifying the supported transcoded profiles. The dict should contain the id of the profile, the command to be executed with the first parameter to be the input and the second the output file, and the list of supported mime types for this profile
	e.g. profiles = [ {'id':'low', 'cmd':'scripts/lowQualityTranscode %s %s', 'supported_mime_types': ['video/mpeg', 'video/3gpp'] } ]
 


Usage
-----

For the moment the only way to see collective.transcode.daemon in full action is to use Plumi 3.0:
    http://plone.org/products/plumi or http://svn.plone.org/svn/collective/plumi.buildout/

We are now working on a generic Plone integration component for collective.transcode.daemon. Note however that there is nothing Plone specific in c.t.d. It shouldn't be hard to integrate it in any other content management framework.


