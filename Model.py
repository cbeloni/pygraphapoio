#!/usr/bin/env python
# coding: utf-8
import cx_Oracle

class ConOracle:
    def __init__(self):
        self.con = cx_Oracle.connect('hr/hr@192.168.0.104/xe')
        self.cur = self.con.cursor()

    def execute(self, query):
        self.cur.execute(query)
        print (self.cur)
        return self.cur    

    def fechar(self):  
        self.cur.close()
        self.con.close()           
