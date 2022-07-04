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


    def excluir_produto(self):
        self.listar_produtos_normal()
        entry = int(input('Insira o código do produto: '))
        for i in range(len(self.listaProdutos)):
            if self.listaProdutos[i].cod == entry:
                self.listaProdutos.pop(i)
                print('\nProduto excluido com sucesso!!!\n')
                break
            else:
                pass
    
    def lista_pqp(self):
        print('Listar por:\n'
              '1 - Codígo\n'
              '2 - Nome\n'
              '3 - Fabricante\n')
        entry = str(input('Digite o N° da opção:'))
        if entry == '1':
            num = int(input('Digite o Código solicitado: '))
            for i in range(len(self.listaProdutos)):
                if num == self.listaProdutos[i].cod:
                    print('---------------------------------------------------------------------\n'
                    'Código:', self.listaProdutos[i].cod,', Produto: ',self.listaProdutos[i].nome,', Fabricante:', self.listaProdutos[i].fabr, ', Quantidade:', self.listaProdutos[i].quant,'\n'
                        '---------------------------------------------------------------------\n')
                else: pass

        elif entry == '2':
            nome = str(input('Digite o Nome do produto solicitado: '))
            for i in range(len(self.listaProdutos)):
                if nome == self.listaProdutos[i].nome:
                    print('---------------------------------------------------------------------\n'
                    'Código:', self.listaProdutos[i].cod,', Produto: ',self.listaProdutos[i].nome,', Fabricante:', self.listaProdutos[i].fabr, ', Quantidade:', self.listaProdutos[i].quant,'\n'
                    '---------------------------------------------------------------------\n')  
                else: pass

        elif entry == '3':
            fabr = str(input('Digite o Nome do Fabricante solicitado: '))
            for i in range(len(self.listaProdutos)):
                if fabr == self.listaProdutos[i].fabr:
                    print('---------------------------------------------------------------------\n'
                    'Código:', self.listaProdutos[i].cod,', Produto: ',self.listaProdutos[i].nome,', Fabricante:', self.listaProdutos[i].fabr, ', Quantidade:', self.listaProdutos[i].quant,'\n'
                    '---------------------------------------------------------------------\n')
                else: pass

        else: 
            for i in range(len(self.listaProdutos)):
                print('---------------------------------------------------------------------\n'
                'Código:', self.listaProdutos[i].cod,', Produto: ',self.listaProdutos[i].nome,', Fabricante:', self.listaProdutos[i].fabr, ', Quantidade:', self.listaProdutos[i].quant,'\n'
                    '---------------------------------------------------------------------\n')
        
    def listar_produtos_normal(self):
        for i in range(len(self.listaProdutos)):
            print('---------------------------------------------------------------------\n'
            'Código:', self.listaProdutos[i].cod,', Produto: ',self.listaProdutos[i].nome,', Fabricante:', self.listaProdutos[i].fabr, ', Quantidade:', self.listaProdutos[i].quant,'\n'
                  '---------------------------------------------------------------------\n')
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

    def excluir_fabr(self):
        self.listar_fabr_normal()
        entry = int(input('Insira o código do Fabricante: '))
        for i in range(len(self.listaFabricante)):
            if self.listaFabricante[i].cod == entry:
                self.listaFabricante.pop(i)
                print('\nFabricante excluido com sucesso!!!\n')
                break
            else:
                pass



    def lista_pqp_fabr(self):
        print('Listar por:\n'
              '1 - Codígo\n'
              '2 - Nome\n'
              '3 - CNPJ\n')

        entry = str(input('Digite o N° da opção:'))
        if entry == '1':
            cod = int(input('Digite o Código solicitado: '))
            for i in range(len(self.listaFabricante)):
                if cod == self.listaFabricante[i].cod:
                    print('-----------------------------------------------------------------------------------------\n'
                        'Código:', self.listaFabricante[i].cod,', Fabricante: ',self.listaFabricante[i].nome,', CNPJ:', self.listaFabricante[i].cnpj, ', Endereço:', self.listaFabricante[i].local,'\n'
                        '-----------------------------------------------------------------------------------------\n')
                else: pass

        elif entry == '2':
            name = str(input('Digite o Nome do produto solicitado: '))
            for i in range(len(self.listaFabricante)):
                if name == self.listaFabricante[i].nome:
                    print('-----------------------------------------------------------------------------------------\n'
                        'Código:', self.listaFabricante[i].cod,', Fabricante: ',self.listaFabricante[i].nome,', CNPJ:', self.listaFabricante[i].cnpj, ', Endereço:', self.listaFabricante[i].local,'\n'
                        '-----------------------------------------------------------------------------------------\n')  
                else: pass

        elif entry == '3':
            cnpj = str(input('Digite o Nome do Fabricante solicitado: '))
            for i in range(len(self.listaFabricante)):
                if cnpj == self.listaFabricante[i].cnpj:
                    print('-----------------------------------------------------------------------------------------\n'
                        'Código:', self.listaFabricante[i].cod,', Fabricante: ',self.listaFabricante[i].nome,', CNPJ:', self.listaFabricante[i].cnpj, ', Endereço:', self.listaFabricante[i].local,'\n'
                        '-----------------------------------------------------------------------------------------\n')
                else: pass

        else: 
            for i in range(len(self.listaFabricante)):
                    print('-----------------------------------------------------------------------------------------\n'
                        'Código:', self.listaFabricante[i].cod,', Fabricante: ',self.listaFabricante[i].nome,', CNPJ:', self.listaFabricante[i].cnpj, ', Endereço:', self.listaFabricante[i].local,'\n'
                        '-----------------------------------------------------------------------------------------\n')