from ntpath import realpath
from class_produto import *

class Estoque:
    def __init__(self):
        self.listaProdutos = []
    
    def cadastrar_produto(self):
        self.listaProdutos.append(Produto())
    
    def listar_produtos(self):
        for i in range(len(self.listaProdutos)):
            print('Código do produto: ', self.listaProdutos[i].cod,
            '\nNome do Produto: ',self.listaProdutos[i].nome,
            '\nDescrição do Produto: ', self.listaProdutos[i].desc,
            '\nFabricante: ', self.listaProdutos[i].fabr,
            '\nQuantidade em Estoque: ',self.listaProdutos[i].quant,'\n')
    
    def listar_por_cod(self):
        resp = input('Digite o ID para pesquisa')
        for i in range(len(self.listaProdutos)):
            if resp == self.listaProdutos[i].cod:
             print('Código do produto: ', self.listaProdutos[i].cod,
            '\nNome do Produto: ',self.listaProdutos[i].nome,
            '\nDescrição do Produto: ', self.listaProdutos[i].desc,
            '\nFabricante: ', self.listaProdutos[i].fabr,
            '\nQuantidade em Estoque: ',self.listaProdutos[i].quant,'\n')

    def alter_desc(self):
        resp = input('Digite o ID do produto: ')

        for i in range(len(self.listaProdutos)):
            if resp == self.listaProdutos[i].cod:
                self.listaProdutos[i].nome= input('Digite o novo Nome ')
                self.listaProdutos[i].desc= input('Digite a nova Descrição ')

    def listar(self):
        for i in  range(len(self.listaProdutos)):

            print('Código: ', self.listaProdutos[i].cod,
            'Descriçao:', self.listaProdutos[i].desc,
            'Fabricante: ', self.listaProdutos[i].fabr,
            'Quantidade:', self.listaProdutos[i].quant)

        resp=input('Insira o codigo do produto:\n')

        for i in range(len(self.listaProdutos)):
            if resp == self.listaProdutos[i].cod:
                print('Código: ', self.listaProdutos[i].cod,
                'Descriçao:', self.listaProdutos[i].desc,
                'Fabricante: ', self.listaProdutos[i].fabr,
                'Quantidade:', self.listaProdutos[i].quant)
            else:
                 pass

        
