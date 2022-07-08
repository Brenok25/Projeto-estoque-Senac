from class_new_estoque import *
from class_compra import *
from class_new_venda import *

class Menu:
    def __init__(self):
        estoque = DBAestoque()

        venda = Venda()
        venda.entrada = estoque

        print('BEM VINDO AO SEU APLICATIVO DE ESTOQUE')
        while True:
            print('\nO que deseja fazer hoje?')
            entrada = str(input(
                  '\n 1 - Cadastrar'
                  '\n 2 - Listagens'
                  '\n 3 - Atualizar informações'
                  '\n 4 - Exclusões'
                  '\n 5 - Compras efetuadas'
                  '\n 6 - Vendas efetuadas\n'))
            
            if entrada == '1':
                num1 = str(input('Deseja:\n'
                                 '1 - Cadastrar Novo Produto\n'
                                 '2 - Cadastrar Novo Fabricante\n'))
                
                if num1 == '1':
                    cod = None
                    nome = input('Entre com o Nome do produto: ')
                    fabr = input('Entre com o nome do fabricante: ')
                    estoque.salva_produto(cod, nome, fabr)
                
                elif num1 == '2':
                    cod = None
                    nome = input('Entre com o Nome do Fabricante: ')
                    cnpj = input('Entre com o CNPJ do fabricante: ')
                    local = input('Entre com o Endereço do fabricante: ')
                    estoque.salva_fabricante(cod, nome, cnpj, local)
                
                else: pass
            
            elif entrada == '2':
                num2 = str(input('Deseja:\n'
                                 '1 - Listar Produtos\n'
                                 '2 - Listar Fabricante\n'))

                if num2 == '1':
                    tabela = 'Produto'
                    estoque.listar(tabela)
                
                elif num2 == '2':
                    tabela = 'Fabricante'
                    estoque.listar(tabela)

                else: pass
            
            elif entrada == '3':
                num3 = str(input('Deseja:\n'
                                 '1 - Alterar descrição de Produto\n'
                                 '2 - Alterar descrição de  Fabricante\n'))

                if num3 == '1':
                    cod = int(input('Informe o código do Produto: '))
                    valor = input('Entre com o novo Nome:')
                    tabela = 'Produto'
                    atributo = 'nome'
                    estoque.alterar_descricao(tabela, atributo, valor, cod)
                
                elif num3 == '2':
                    cod = int(input('Informe o código do Fabricante: '))
                    valor = input('Entre com o novo Nome:')
                    tabela = 'Fabricante'
                    atributo = 'nome'
                    estoque.alterar_descricao(tabela, atributo, valor, cod)
                

                else: pass

            elif entrada == '4':
                num4 = str(input('Deseja:\n'
                                 '1 - Excluir Produto\n'
                                 '2 - Excluir  Fabricante\n'))

                if num4 == '1':
                    cod = int(input('Informe o código do Produto: '))
                    tabela = 'Produto'
                    estoque.deletar(tabela,cod)
                
                elif num4 == '2':
                    cod = int(input('Informe o código do Fabricante: '))
                    tabela = 'Fabricante'
                    estoque.deletar(cod, tabela)

                else: pass
            
            elif entrada == '5':
                num5 = str(input('Deseja:\n'
                                 '1 - Comprar Produto\n'
                                 '2 - listar transações\n'))

                if num5 == '1':
                    cod = int(input('Informe o código do Produto: '))
                    value =  int(input('Informe a quantidade comprada: '))
                    estoque.compra(cod, value)
                
                elif num5 == '2':
                    pass

                else: pass

            elif entrada == '6':
                num6 = str(input('Deseja:\n'
                                 '1 - Vender Produto\n'
                                 '2 - listar transações\n'))

                if num6 == '1':
                    venda.vender()
                
                elif num6 == '2':
                    venda.movimenta()

                else: pass
            
            elif entrada == '10':
                    cod = int(input('Informe o código do Produto: '))
                    value = int(input('Informe a quantidade do Produto comprado: '))
                    venda.vender(cod,value)
            
            elif entrada == '0':
                print('Obrigado por usar nosso sistema, volte sempre!')
                break

            else: pass
                                                 