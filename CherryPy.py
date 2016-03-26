## -*- coding: utf-8 -*-
import cherrypy
from mako.template import Template
from Grafico import GrafLinha
from Model import ConOracle
import os

class Home(object):
    def __init__(self):
        self.nome_tabela = 'bko_apoio_6884'

    def index(self):
        con_oracle = ConOracle('adminprov2_10/adminpro@172.22.4.30/bda')
        valores, indice = con_oracle.dados_process_not_null(self.nome_tabela)
        valores_pendentes = con_oracle.dados_process_null(self.nome_tabela)
        con_oracle.fechar()

        titulo = '''Registros processados: %s \n 
                    Registros pendentes: %s ''' % (sum(valores),sum(valores_pendentes))
        graf = GrafLinha(indice,titulo )        
        graf.adicionar_linha(self.nome_tabela,valores)
        graf.renderizar_arquivo('./public/graf.svg')

        tmpl = Template(filename='index.html')
        return tmpl.render()
    index.exposed = True

    def tabela(self, nome_tabela):
        self.nome_tabela = nome_tabela

        return self.index()
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