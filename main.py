#!/usr/bin/env python
# coding: utf-8
from CherryPy import Home
import cherrypy
import os

class Main(Home):
    def __init__(self): 
        super(Main, self).__init__()

if __name__ == '__main__':
    conf = {
       '/': {
           'tools.sessions.on': True,
           'tools.staticdir.root': os.path.abspath(os.getcwd())
       },
       '/static': {
           'tools.staticdir.on': True,
           'tools.staticdir.dir': './public'
       }
    }        

    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': 8080,
                           })
    cherrypy.quickstart(Main(), '/' , conf)        