#!/usr/bin/env python
# coding: utf-8
import pygal
from pygal.style import NeonStyle

class GrafLinha:
    '''
    Renderizar gráfico.
    '''
    def __init__(self, periodo,titulo):
        self.periodo = periodo        
        self.line_chart = pygal.Line(explicit_size=True, width=900, height=600, fill=True, interpolate='cubic', style=NeonStyle)        
        self.line_chart.title =  titulo
        self.line_chart.x_labels = map(str, self.periodo)
    
    def adicionar_linha(self,nome, valores):
        '''
        Nome: item a ser adicionado como gráfico
        valores: lista com os valores a serem incrementados
        '''
        self.line_chart.add(nome,  valores) 
        
    def renderizar_arquivo(self,nome_arquivo):
        self.line_chart.render_to_file(nome_arquivo)

    def __repr__(self):
        '''
        Retorna gráfico renderizado.
        '''
        return self.line_chart.render()    

    def __str__(self):
        return self.line_chart.render()            

if __name__ == '__main__':
    graf = GrafLinha(range(2002, 2013), 'Browser usage evolution (in %)')
    graf.adicionar_linha('Firefox',[None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    graf.adicionar_linha('Chrome', [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    graf.adicionar_linha('IE',     [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    graf.adicionar_linha('Others', [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    graf.line_chart.render_to_file('linha_chart.svg')