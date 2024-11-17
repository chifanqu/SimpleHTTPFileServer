# !/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages
    
setup(
    name = "SimpleHTTPFileServer",
    version = "0.2",
    py_modules=['SimpleHTTPFileServer'],
    
    packages = ['SimpleHTTPFileServer2','SimpleHTTPFileServer3'],
    
    description = "Simple HTTP Server With POST and PUT Upload.",
    long_description = "Simple HTTP Server With POST and PUT Upload.",
    author = "chifanqu",
    author_email = "yiyiyaya1@139.com",

    python_requires='>=2.7',

    keywords = ("file server", "put"),
    platforms = "Independant",
    url = "https://github.com/chifanqu/SimpleHTTPFileServer",
    entry_points = {
        'console_scripts': [
            'SimpleHTTPFileServer = SimpleHTTPFileServer:main'
        ]
    }
)
