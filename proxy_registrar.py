#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Programa Proxy registrar
"""
 
import socketserver
import sys

if __name__ == "__main__":
    try:
    	config = int(sys.argv[1])
	except:
		sys.exit("Usage: python proxy_registrar.py config")
	print('Server ' + USER + ' listening at port ' + PORT + '...')

