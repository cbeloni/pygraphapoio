#!/usr/bin/env python
# coding: utf-8
from Grafico import GrafLinha
from CherryPy import Home
import cherrypy
import os
import cx_Oracle
con = cx_Oracle.connect('hr/hr@192.168.0.104/xe')
cur = con.cursor()
cur.execute("SELECT count(1),to_char(process_date,'hh24:mi dd/mm/yyyy') FROM sys.bko_apoio_0001 group by to_char(process_date,'hh24:mi dd/mm/yyyy')  order by 2 asc")    
valores = []
indice = []

for result in cur:
    valores.append(result[0])
    indice.append(result[1])
print valores    
cur.close()
con.close() 

class Main(Home):
    def __init__(self): 
        graf = GrafLinha(indice, 'Browser usage evolution (in %)')
        graf.adicionar_linha('Dados',valores)
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