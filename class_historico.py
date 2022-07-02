

class Historico:
    def __init__(self):
        self.transacoes = []

    def histo(self):
        print('Transações: ')
        for i in self.transacoes:
            print('--', i)