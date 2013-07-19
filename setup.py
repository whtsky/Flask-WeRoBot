"""
Flask-WeRoBot
---------------

Adds WeRoBot support to Flask.

:copyright: (c) 2013 by whtsky.
:license: BSD, see LICENSE for more details.

Links
`````

* `documentation <https://flask-werobot.readthedocs.org/>`_
"""

from setuptools import setup

setup(
    name='Flask-WeRoBot',
    version='0.1.2',
    url='https://github.com/whtsky/Flask-WeRoBot',
    license='BSD',
    author='whtsky',
    author_email='whtsky@gmail.com',
    description='Writing WeChat Robot by WeRoBot in Flask.',
    long_description=__doc__,
    py_modules=['flask_werobot'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'WeRoBot>=0.3.5'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
