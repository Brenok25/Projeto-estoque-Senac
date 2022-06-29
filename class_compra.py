
from class_estoque import *

class Compra:

    def __init__(self): #Self é convenção
        self.entrada = Estoque()

    def comprar(self):
        entry = int(input('Cod do produto: '))
        for i in range(len(self.entrada.listaProdutos)):
            if entry == self.entrada.listaProdutos[i].cod:
                self.entrada.listaProdutos[i].quant += int(input('Quantidade comprada: '))
    

