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

        while True: 
            entrada = input('\n'
                            ' 1 - Cadastrar Produto\n'
                            ' 2 - Listar Produtos\n'
                            ' 3 - Alterar Descrição\n'
                            ' 4 - Excluir Produto\n'
                            ' 5 - Cadastrar Fabricante\n'
                            ' 6 - Listar Fabricantes\n'
                            ' 7 - Alterar dados Fabricante\n'
                            ' 8 - Excluir Fabricante\n'
                            ' 9 - Comprar\n'
                            ' 10 - Historico compras\n'
                            ' 11 - Vender\n'
                            ' 12 - Historico vendas\n'
                            ' 0 - Sair\n')

            if entrada == '1':
                estoque.cadastrar_produto()
            
            elif entrada == '2':
                estoque.lista_pqp()

            elif entrada == '3':
                estoque.alter_desc()

            elif entrada == '4':
                estoque.excluir_produto()

            elif entrada == '5':
                estoque.cadastrar_fabr()

            elif entrada == '6':
                estoque.lista_pqp_fabr()

            elif entrada == '7':
                estoque.alter_fabr()

            elif entrada == '8':
                estoque.excluir_fabr()

            elif entrada == '9':
                compra.comprar()

            elif entrada == '10':
                compra.movimenta()
 
            elif entrada == '11':
                venda.vender()
            
            elif entrada == '12':
                venda.movimenta()

            elif entrada == '0':
                print('Obrigado por usar nossos serviços, volte sempre\n')
                break

            else:
                print('Opção invalida, tente novamente')