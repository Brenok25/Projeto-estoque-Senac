from tracemalloc import stop
from class_new_estoque import *
from class_new_compra import *
from class_new_venda import *

class Menu:
    def __init__(self):
        estoque = DBAestoque()

        compra = Compra()
        compra.entrada = estoque

        venda = Venda()        

        print('BEM VINDO AO SEU APLICATIVO DE ESTOQUE')
        while True:
            print('\nO que deseja fazer hoje?')
            entrada = str(input(
                  '\n 1 - Cadastrar'
                  '\n 2 - Listagens'
                  '\n 3 - Atualizar informações'
                  '\n 4 - Exclusões'
                  '\n 5 - Comprar Produto'
                  '\n 6 - Vender Produto\n'))
            
            if entrada == '1':
                num1 = str(input('Deseja:\n'
                                 '1 - Cadastrar Novo Produto\n'
                                 '2 - Cadastrar Novo Fabricante\n'
                                 '0 - Voltar\n'))

                
                if num1 == '1':
                    cod = None
                    nome = input('Entre com o Nome do produto: ')
                    atributo = 'Fabricante'
                    estoque.listar(atributo)
                    fabr = int(input('Entre com o ID do fabricante: '))
                    estoque.salva_produto(cod, nome, fabr)
                
                elif num1 == '2':
                    cod = None
                    nome = input('Entre com o Nome do Fabricante: ')
                    cnpj = input('Entre com o CNPJ do fabricante: ')
                    local = input('Entre com o Endereço do fabricante: ')
                    estoque.salva_fabricante(cod, nome, cnpj, local)
                
                elif num1 == '0':
                    pass
                
                else: pass
            
            elif entrada == '2':
                num2 = str(input('Deseja:\n'
                                 '1 - Listar Produtos\n'
                                 '2 - Listar Fabricante\n'
                                 '0 - Voltar\n'))

                if num2 == '1':
                    tabela = 'Produto'
                    estoque.listar(tabela)
                
                elif num2 == '2':
                    tabela = 'Fabricante'
                    estoque.listar(tabela)
                
                elif num2 == '0':
                    pass

                else: pass
            
            elif entrada == '3':
                num3 = str(input('Deseja:\n'
                                 '1 - Alterar descrição de Produto\n'
                                 '2 - Alterar descrição de  Fabricante\n'
                                 '0 - Voltar\n'))

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
                
                elif num3 == '0':
                    pass
                

                else: pass

            elif entrada == '4':
                num4 = str(input('Deseja:\n'
                                 '1 - Excluir Produto\n'
                                 '2 - Excluir  Fabricante\n'
                                 '0 - Voltar\n'))

                if num4 == '1':
                    cod = int(input('Informe o código do Produto: '))
                    tabela = 'Produto'
                    estoque.deletar(tabela,cod)
                
                elif num4 == '2':
                    cod = int(input('Informe o código do Fabricante: '))
                    tabela = 'Fabricante'
                    estoque.deletar(cod, tabela)
                
                elif num4 == '0':
                    pass

                else: pass
            
            elif entrada == '5':
                num5 = str(input('Deseja:\n'
                                 '1 - Comprar Produto\n'
                                 '2 - listar transações\n'
                                 '0 - Voltar\n'))

                if num5 == '1':
                    cod = int(input('Informe o código do Produto: '))
                    value = int(input('Informe a quantidade do Produto comprado: '))
                    atributo = 'compra'
                    compra.compra(cod,value,atributo)
                
                elif num5 == '2':
                    pass

                elif num5 == '0':
                    pass


                else: pass

            elif entrada == '6':
                num6 = str(input('Deseja:\n'
                                 '1 - Vender Produto\n'
                                 '2 - listar transações\n'
                                 '0 - Voltar\n'))

                if num6 == '1':
                    cod = int(input('Informe o código do Produto: '))
                    value = int(input('Informe a quantidade do Produto vendido: '))
                    atributo = 'venda'
                    venda.venda(cod,value,atributo)
                
                elif num6 == '2':
                    venda.movimenta()

                elif num6 == '0':
                    pass

                else: pass

            # elif entrada == '10':
            #         teste né boy


            elif entrada == '0':
                print('Obrigado por usar nosso sistema, volte sempre!')
                break

            else: pass
                                                 