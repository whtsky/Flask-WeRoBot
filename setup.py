from setuptools import setup
import flask_werobot

setup(
    name='Flask-WeRoBot',
    version=flask_werobot.__version__,
    url='https://github.com/whtsky/Flask-WeRoBot',
    license='BSD',
    author='whtsky',
    author_email='whtsky@gmail.com',
    description='Writing WeChat Robot by WeRoBot in Flask.',
    long_description=flask_werobot.__doc__,
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
