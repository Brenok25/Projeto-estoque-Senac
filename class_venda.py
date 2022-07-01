from class_estoque import *


class Venda:

    def __init__(self): #Self é convenção
        self.entrada = Estoque()

    def vender(self):
        entry = int(input('Cod do produto vendido: '))
        for i in range(len(self.entrada.listaProdutos)):
            if entry == self.entrada.listaProdutos[i].cod:
                if self.entrada.listaProdutos[i].quant == 0:
                    print('Não possuimos em estoque o item desejado')
                else:
                    self.entrada.listaProdutos[i].quant -= int(input('Quantidade vendida: '))