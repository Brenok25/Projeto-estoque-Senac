from class_estoque import *
from class_historico import *


class Venda:

    def __init__(self): #Self é convenção
        self.entrada = Estoque()
        self.historico = Historico()

    def vender(self):
        entry = int(input('Cod do produto vendido: '))
        for i in range(len(self.entrada.listaProdutos)):
            if entry == self.entrada.listaProdutos[i].cod:
                if self.entrada.listaProdutos[i].quant == 0:
                    print('Não possuimos em estoque o item desejado')
                else:
                    x = int(input('Quantidade comprada: '))
                    self.entrada.listaProdutos[i].quant -= x
                    self.historico.transacoes.append(f'Venda de {x} unidades do produto: {self.entrada.listaProdutos[i].nome} / Código: {self.entrada.listaProdutos[i].cod}')

    def movimenta(self):
        print(self.historico.histo())