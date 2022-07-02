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
            entrada = input(' 1 - Cadastrar\n 2 - Listar Produtos\n 3 - Alterar Descrição\n 4 - Comprar\n 5 - Vender\n 0 - Sair\n')

            if entrada == '1':
                estoque.cadastrar_produto()
            
            elif entrada == '2':
                estoque.listar()

            elif entrada == '3':
                estoque.alter_desc()

            elif entrada == '4':
                compra.comprar()
            
            elif entrada == '5':
                venda.vender()

            elif entrada == '0':
                print('Obrigado por usar nossos serviços, volte sempre\n')
                break

            else:
                print('Opção invalida, tente novamente')