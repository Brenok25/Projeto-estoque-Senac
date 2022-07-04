from ast import Pass
from class_estoque import *
from class_compra import *
from class_venda import *

class Menu:
    def __init__(self):
        estoque = Estoque()

        compra = Compra()
        compra.entrada = estoque

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
                    estoque.cadastrar_produto()
                
                elif num1 == '2':
                    estoque.cadastrar_fabr()
                
                else: pass
            
            elif entrada == '2':
                num2 = str(input('Deseja:\n'
                                 '1 - Listar Produtos\n'
                                 '2 - Listar Fabricante\n'))

                if num2 == '1':
                    estoque.lista_pqp()
                
                elif num2 == '2':
                    estoque.lista_pqp_fabr()

                else: pass
            
            elif entrada == '3':
                num3 = str(input('Deseja:\n'
                                 '1 - Alterar descrição de Produto\n'
                                 '2 - Alterar descrição de  Fabricante\n'))

                if num3 == '1':
                    estoque.alter_desc()
                
                elif num3 == '2':
                    estoque.alter_fabr()

                else: pass

            elif entrada == '4':
                num4 = str(input('Deseja:\n'
                                 '1 - Excluir Produto\n'
                                 '2 - Excluir  Fabricante\n'))

                if num4 == '1':
                    estoque.excluir_produto()
                
                elif num4 == '2':
                    estoque.excluir_fabr()

                else: pass
            
            elif entrada == '5':
                num5 = str(input('Deseja:\n'
                                 '1 - Comprar Produto\n'
                                 '2 - listar transações\n'))

                if num5 == '1':
                    compra.comprar()
                
                elif num5 == '2':
                    compra.movimenta()

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
            
            elif entrada == '0':
                print('Obrigado por usar nosso sistema, volte sempre!')
                break

            else: pass
                                                 