# -*- coding: utf-8 -*-
"""
This module contains the tool of collective.transcode.recipe
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1'

long_description = (
    read('collective/transcode/recipe/README.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('collective', 'transcode', 'recipe', 'README.txt')
    + '\n' +
    'Contributors\n' 
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' + 
    read('CHANGES.txt')
    + '\n' +
   'Download\n'
    '********\n'
    )
entry_point = 'collective.transcode.recipe:Recipe'
entry_points = {"zc.buildout": ["default = %s" % entry_point]}

tests_require=['zope.testing', 'zc.buildout']

setup(name='collective.transcode.recipe',
      version=version,
      description="Recipe to setup a transcode daemon",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='video plone zope transcoding recipe',
      author='unweb.me',
      author_email='we@unweb.me',
      url='https://unweb.me',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.transcode'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
						'zope.testing',
                        'zc.buildout',
						'zc.recipe.egg',
                        # -*- Extra requirements: -*-
                        'py',
                        'collective.transcode.daemon',
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'collective.transcode.recipe.tests.test_docs.test_suite',
      entry_points=entry_points,
      )
