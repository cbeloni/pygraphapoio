## -*- coding: utf-8 -*-
import cherrypy
from mako.template import Template
import os

class Home(object):
    def index(self):
        tmpl = Template(filename='index.html')
        return tmpl.render()
    index.exposed = True

    def tabela(self, nome_tabela):
        self.nome_tabela = nome_tabela

        return self.nome_tabela
    tabela.exposed = True

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
    cherrypy.quickstart(Home(), '/' , conf)