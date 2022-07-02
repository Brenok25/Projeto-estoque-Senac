from ntpath import realpath
from class_produto import *
from class_fabricante import *

class Estoque:
    def __init__(self):
        self.listaProdutos = []
        self.listaProdutos.append(Produto(1,'Notebook','Dell'))
        self.listaProdutos.append(Produto(2,'Monitor','Aoc'))

        self.listaFabricante = []
        self.listaFabricante.append(Fabricante(1, 'Dell', '1234567', 'Narnia, poste de outro mundo' ))
        self.listaFabricante.append(Fabricante(2, 'Aoc', '87512659', 'Gormit, Ilha de lava' ))
    
    def cadastrar_produto(self):
        arg_1 = len(self.listaProdutos)+1
        arg_2 = input('Digite o Nome do produto: ')

        self.listar_fabr_normal()

        arg_3 = int(input('Digite o cod do Fabricante: '))

        for i in range(len(self.listaFabricante)):
            if self.listaFabricante[i].cod == arg_3:
                self.listaProdutos.append(Produto(cod = arg_1,nome = arg_2, fabr =self.listaFabricante[i].nome))
                break
    def alter_desc(self):
        resp = int(input('Digite o ID do produto: '))

        for i in range(len(self.listaProdutos)):
            if resp == self.listaProdutos[i].cod:
                self.listaProdutos[i].nome= input('Digite o novo Nome ')

    def listar(self):
        for i in  range(len(self.listaProdutos)):

            print('---------------------------------------------------------------------\n'
            'Código:', self.listaProdutos[i].cod,', Produto: ',self.listaProdutos[i].nome,', Fabricante:', self.listaProdutos[i].fabr, ', Quantidade:', self.listaProdutos[i].quant,'\n'
                  '---------------------------------------------------------------------\n')

        resp=int(input('Insira o codigo do produto:\n'))

        for i in range(len(self.listaProdutos)):
            if resp == self.listaProdutos[i].cod:
                print('---------------------------------------------------------------------\n'
                'Código:', self.listaProdutos[i].cod,', Produto: ',self.listaProdutos[i].nome,', Fabricante:', self.listaProdutos[i].fabr, ', Quantidade:', self.listaProdutos[i].quant,'\n'
                '---------------------------------------------------------------------\n')
            else:
                pass
    
   # Fabricante
        
    
    def cadastrar_fabr(self):
        arg_1 = len(self.listaFabricante)+1
        arg_2 = input('Digite o Nome do Fabricante: ')
        arg_3 = input('Digite o CNPJ do Fabricante: ')
        arg_4 = input('Digite o Endereço do Fabricante: ')

        self.listaFabricante.append(Fabricante(cod = arg_1, nome = arg_2, cnpj = arg_3, local= arg_4 ))
    

    def alter_fabr(self):
        resp = int(input('Digite o ID do Fabricante: '))

        for i in range(len(self.listaFabricante)):
            if resp == self.listaFabricante[i].cod:
                self.listaFabricante[i].nome = input('Digite o novo Nome ')

    def listar_fabr(self):
        for i in  range(len(self.listaFabricante)):

            print('-----------------------------------------------------------------------------------------\n'
            'Código:', self.listaFabricante[i].cod,', Fabricante: ',self.listaFabricante[i].nome,', CNPJ:', self.listaFabricante[i].cnpj, ', Endereço:', self.listaFabricante[i].local,'\n'
                  '-----------------------------------------------------------------------------------------\n')

        resp=int(input('Insira o codigo do produto:\n'))

        for i in range(len(self.listaFabricante)):
            if resp == self.listaFabricante[i].cod:
                print('-----------------------------------------------------------------------------------------\n'
                'Código:', self.listaFabricante[i].cod,', Fabricante: ',self.listaFabricante[i].nome,', CNPJ:', self.listaFabricante[i].cnpj, ', Endereço:', self.listaFabricante[i].local,'\n'
                '-----------------------------------------------------------------------------------------\n')
            else:
                 pass

    def listar_fabr_normal(self):
        for i in range(len(self.listaProdutos)):
            print('-----------------------------------------------------------------------------------------\n'
                'Código:', self.listaFabricante[i].cod,', Fabricante: ',self.listaFabricante[i].nome,', CNPJ:', self.listaFabricante[i].cnpj, ', Endereço:', self.listaFabricante[i].local,'\n'
                '-----------------------------------------------------------------------------------------\n')


    
    # def listar_produtos(self):
    #     for i in range(len(self.listaProdutos)):
    #         print('Código do produto: ', self.listaProdutos[i].cod,
    #         '\nNome do Produto: ',self.listaProdutos[i].nome,
    #         '\nFabricante: ', self.listaProdutos[i].fabr,
    #         '\nQuantidade em Estoque: ',self.listaProdutos[i].quant,'\n')
    
    # def listar_por_cod(self):
    #     resp = input('Digite o ID para pesquisa')
    #     for i in range(len(self.listaProdutos)):
    #         if resp == self.listaProdutos[i].cod:
    #          print('Código do produto: ', self.listaProdutos[i].cod,
    #         '\nNome do Produto: ',self.listaProdutos[i].nome,
    #         '\nFabricante: ', self.listaProdutos[i].fabr,
    #         '\nQuantidade em Estoque: ',self.listaProdutos[i].quant,'\n')