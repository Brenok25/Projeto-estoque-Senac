from class_estoque import *
from class_compra import *

class Menu:
    def __init__(self):
        estoque = Estoque()
        compra = Compra()
        compra.entrada = estoque

        while True: 
            entrada = input(' 1 - Novo Cadastro\n 2 - Listar produtos no sistema\n 3 - Filtrar Produtos\n 3 - Alterar Nome e descrição de poduto\n 4 - Comprar\n 0 - Sair \n')

            if entrada == '1':
                estoque.cadastrar_produto()
            
            elif entrada == '2':
                estoque.listar_produtos()

            elif entrada == '3':
                estoque.listar()
            
            elif entrada == '3':
                estoque.alter_desc()

            elif entrada == '4':
                compra.comprar()

            else:
                break