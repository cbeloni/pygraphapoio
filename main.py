#!/usr/bin/env python
# coding: utf-8
from Grafico import GrafLinha
from CherryPy import Home
import cherrypy
import os

class Main(Home):
    def __init__(self):
        graf = GrafLinha(range(2002, 2013), 'Browser usage evolution (in %)')
        graf.adicionar_linha('Firefox',[None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
        graf.adicionar_linha('Chrome', [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
        graf.adicionar_linha('IE',     [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
        graf.adicionar_linha('Others', [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
        graf.renderizar_arquivo('./public/graf.svg')

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