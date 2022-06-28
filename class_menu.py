from class_estoque import *

class Menu:
    def __init__(self):
        estoque = Estoque()

        while True: 
            entrada = input(' 1 - Novo Cadastro\n 2 - Listar produtos no sistema\n 3 - Procurar Produto\n 4 - Alterar Nome e descrição de poduto\n')

            if entrada == '1':
                estoque.cadastrar_produto()
            
            elif entrada == '2':
                estoque.listar_produtos()

            elif entrada == '3':
                estoque.listar_por_cod()
            
            elif entrada == '4':
                estoque.alter_desc()
            
            elif entrada == '5':
                estoque.listar()

            else:
                break