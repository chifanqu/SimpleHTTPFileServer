#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

def main():
    py_version = sys.version
    if py_version[0] == '2':
        from SimpleHTTPFileServer2 import main
        main()
    elif py_version[0] == '3':
        from SimpleHTTPFileServer3 import main
        main()
    else:
        print("Python version error: %s" % py_version)
