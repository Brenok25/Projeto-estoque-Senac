from ntpath import realpath
from class_produto import *

class Estoque:
    def __init__(self):
        self.listaProdutos = []
        self.listaProdutos.append(Produto('1','Notebook','Dell'))
        self.listaProdutos.append(Produto('2','Monitor','Aoc'))
    
    def cadastrar_produto(self):
        arg_1 = len(self.listaProdutos)+1
        arg_2 = input('Digite o Nome do produto: ')
        arg_3 = input('Digite o Fabricante do produto: ')

        self.listaProdutos.append(Produto(cod = arg_1, nome = arg_2, fabr = arg_3 ))
    
    def listar_produtos(self):
        for i in range(len(self.listaProdutos)):
            print('Código do produto: ', self.listaProdutos[i].cod,
            '\nNome do Produto: ',self.listaProdutos[i].nome,
            '\nFabricante: ', self.listaProdutos[i].fabr,
            '\nQuantidade em Estoque: ',self.listaProdutos[i].quant,'\n')
    
    def listar_por_cod(self):
        resp = input('Digite o ID para pesquisa')
        for i in range(len(self.listaProdutos)):
            if resp == self.listaProdutos[i].cod:
             print('Código do produto: ', self.listaProdutos[i].cod,
            '\nNome do Produto: ',self.listaProdutos[i].nome,
            '\nFabricante: ', self.listaProdutos[i].fabr,
            '\nQuantidade em Estoque: ',self.listaProdutos[i].quant,'\n')

    def alter_desc(self):
        resp = input('Digite o ID do produto: ')

        for i in range(len(self.listaProdutos)):
            if resp == self.listaProdutos[i].cod:
                self.listaProdutos[i].nome= input('Digite o novo Nome ')

    def listar(self):
        for i in  range(len(self.listaProdutos)):

            print('Código: ', self.listaProdutos[i].cod,
            'Fabricante: ', self.listaProdutos[i].fabr,
            'Quantidade:', self.listaProdutos[i].quant)

        resp=input('Insira o codigo do produto:\n')

        for i in range(len(self.listaProdutos)):
            if resp == self.listaProdutos[i].cod:
                print('Código: ', self.listaProdutos[i].cod,
                'Fabricante: ', self.listaProdutos[i].fabr,
                'Quantidade:', self.listaProdutos[i].quant)
            else:
                 pass

