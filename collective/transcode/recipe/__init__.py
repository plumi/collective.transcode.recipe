# -*- coding: utf-8 -*-
"""Recipe transcode daemon - based on darksnow.recipe.convertdaemon"""
import os, re, shutil
import zc.buildout
import zc.recipe.egg

from os.path import abspath, dirname, join, exists
from collective.transcode.daemon.config import listen_host as default_listen_host
from collective.transcode.daemon.config import listen_port as default_listen_port
from collective.transcode.daemon.config import videofolder as default_videofolder
from collective.transcode.daemon.config import profiles as default_profiles
from collective.transcode.daemon.config import secret as default_secret


class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.egg = zc.recipe.egg.Egg(buildout, options['recipe'], options)
        self.buildout, self.options, self.name = buildout, options, name

        options['location'] = os.path.join(
            buildout['buildout']['parts-directory'],
            self.name,
            )
        options['bin-directory'] = buildout['buildout']['bin-directory']


    def install(self):
        """Installer"""
        self.generateStartup() 
        return tuple()

    def update(self):
        """Updater"""
        self.generateStartup()

    def writeConf(self, filename):
        profiles = self.options.get('profiles', default_profiles)
	videofolder = self.options.get('videofolder', default_videofolder)
	host = self.options.get('listen_host', default_listen_host)
        port = self.options.get('listen_port', default_listen_port)
        secret = self.options.get('secret', default_secret)

        conf_file = file(filename, 'w')
	conf_file.write('listen_host = "%s"'% host + '\n')
        conf_file.write('listen_port = "%s"'% port + '\n')
        conf_file.write('secret = "%s"'% secret + '\n')
	conf_file.write('videofolder = "%s"'% videofolder + '\n')
	conf_file.write('profiles = "%s"'% profiles + '\n')
	conf_file.close()


    def prepareVideoFolder(self):
	videofolder = join(self.buildout['buildout']['directory'], self.options.get('videofolder', default_videofolder))

	if not exists(videofolder):
	    os.mkdir(videofolder)


    def preparePartDir(self):
        location = self.options['location']

	transcode_conf = join(location, 'config.py')

        if not exists(location):
            os.mkdir(location)
        self.writeConf(transcode_conf)


    def generateStartup(self):
        options = self.options
        location = options['location']

        bodir = self.buildout['buildout']['directory']

        self.preparePartDir()
	self.prepareVideoFolder()

        extra_paths = options.get('extra-paths', '').split()
        extra_paths.append(bodir)

        requirements, ws = self.egg.working_set(['collective.transcode.recipe'])

        #Generating the script
        zc.buildout.easy_install.scripts(
            [(self.options.get('control-script', self.name),
                'collective.transcode.recipe.ctl', 'main')],
            ws, options['executable'], options['bin-directory'],
            extra_paths = extra_paths,
            #Passing arguments to the ctl main function
            arguments = ('\n        [%r]'
                         '\n        + sys.argv[1:]'
                         % location
                         ),
            #So we can use paths relative to the buildout directory!!
            initialization='import os\nos.chdir("%s")' % bodir,
            )

