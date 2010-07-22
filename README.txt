Introduction
============

A zc.buildout recipe that configures a collective.transcode.daemon instance

For more info check out

- http://pypi.python.org/pypi/collective.transcode.daemon
- http://pypi.python.org/pypi/collective.transcode.star


Supported options
-----------------

The recipe supports the following options:
::

    listen_host
        hostname to listen

    listen_port
        port to use

    videofolder
        relative path of folder where transcoded videos are stored

    secret
        a secret shared key used for authentication and encryption 

    profiles
        a python list of dicts specifying the supported transcoded 
        profiles. The dict should contain
            i) the id of the profile, 
            ii) the command to be executed with the first parameter to be the input and the second the output file
            iii) the list of supported mime types for this profile
        e.g. profiles = [ {'id':'low', 'cmd':'scripts/lowQualityTranscode %s %s', 'supported_mime_types': ['video/mpeg', 'video/3gpp'] } ]
 


