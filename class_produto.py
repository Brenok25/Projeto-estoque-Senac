class Produto:
    def __init__(self):
        self.cod = input('Digite o Código do produto: ')
        self.nome = input('Digite o Nome do produto: ')
        self.desc = input('Digite o Descrição do produto: ')
        self.fabr = input('Digite o Fabricante do produto: ')
        self.quant = input('Digite a Quantidade do produto: ')

        print('O produto foi cadastrado')

