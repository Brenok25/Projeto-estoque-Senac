
# from class_estoque import *
# from class_historico import *

# class Compra:

#     def __init__(self): #Self é convenção
#         self.entrada = Estoque()
#         self.historico = Historico()

#     def comprar(self):
#         entry = int(input('Cod do produto: '))
#         for i in range(len(self.entrada.listaProdutos)):
#             if entry == self.entrada.listaProdutos[i].cod:
#                 x = int(input('Quantidade comprada: '))
#                 self.entrada.listaProdutos[i].quant += x
#                 self.historico.transacoes.append(f'Compra de {x} unidades do produto: {self.entrada.listaProdutos[i].nome} / Código: {self.entrada.listaProdutos[i].cod}')

#     def movimenta(self):
#         print(self.historico.histo())

