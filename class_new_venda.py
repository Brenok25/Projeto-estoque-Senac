
from class_estoque import *
from class_historico import *
import mysql.connector

class Compra:

    def __init__(self):
        self.conexao = mysql.connector.connect(
            host= '127.0.0.1',
            user= 'root',
            password= 'q1w2e3',
            database='estoque_senac'
        )

        self.my_cursor = self.conexao.cursor()
    
    def comprar(self):
        entry = int(input('Cod do produto: '))
        for i in range(len(self.entrada.listaProdutos)):
            if entry == self.entrada.listaProdutos[i].cod:
                x = int(input('Quantidade comprada: '))
                self.entrada.listaProdutos[i].quant += x
                self.historico.transacoes.append(f'Compra de {x} unidades do produto: {self.entrada.listaProdutos[i].nome} / Código: {self.entrada.listaProdutos[i].cod}')

    def movimenta(self):
        print(self.historico.histo())

