## -*- coding: utf-8 -*-
import cherrypy
from mako.template import Template
from Grafico import GrafLinha
from Model import ConOracle
import os

class Home(object):
    def __init__(self):
        self.nome_tabela = 'hr.bko_apoio_0001'

    def index(self):
        ora = self.obter_dados()
        valores, indice = self.valores, self.indice
        ora.fechar()
        titulo = 'Registros processados: %s' % (sum(valores))
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

    def obter_dados(self):
        ora = ConOracle()
        query = """ SELECT count(1),to_char(process_date,'!hh24mi') 
                      FROM %s 
                     where process_status is not null  
                  group by to_char(process_date,'!hh24mi')  order by 2 asc""" % (self.nome_tabela)

        cursor_process_not_null =  ora.execute(query)
        self.valores = []
        self.indice = []
        for result in cursor_process_not_null:
            self.valores.append(result[0])
            self.indice.append(result[1])

        return ora

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