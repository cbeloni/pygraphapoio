#!/usr/bin/env python
# coding: utf-8
import cx_Oracle

class ConOracle:
    def __init__(self,string_conexao):
        self.con = cx_Oracle.connect(string_conexao)
        self.cur = self.con.cursor()

    def execute(self, query):
        self.cur.execute(query)
        return self.cur    

    def dados_process_not_null(self,nome_tabela):
        query = """ SELECT count(1),to_char(process_date,'hh24') 
                      FROM %s 
                     where process_status is not null  
                  group by to_char(process_date,'hh24')  order by 2 asc""" % (nome_tabela)

        cursor_process_not_null =  self.execute(query)

        valores = []
        indice = []
        for result in cursor_process_not_null:
            valores.append(result[0])
            indice.append(result[1])    

        return valores, indice

    def dados_process_null(self,nome_tabela):
        query = """ SELECT count(1) 
                      FROM %s 
                     where process_status is null """ % (nome_tabela)

        cursor_process_null =  self.execute(query)
        valores = []
        for result in cursor_process_null:
            valores.append(result[0])

        return valores

    def fechar(self):  
        self.cur.close()
        self.con.close()           
