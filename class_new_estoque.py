import mysql.connector
from class_produto import *
from class_fabricante import *

class DBAestoque:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host= '127.0.0.1',
            user= 'root',
            password= 'q1w2e3',
            database='estoque_senac'
        )

        self.my_cursor = self.conexao.cursor()
    
    def salva_produto(self, cod, nome, fabr):
        obj_produto = Produto(cod, nome, fabr)
        sql = f'insert into Produto (nome, fabricante) value ("{obj_produto.nome}","{obj_produto.fabr}")'
        self.my_cursor.execute(sql) 
        self.conexao.commit()
    
    def salva_fabricante(self, cod, nome, cnpj, local):
        obj_fabricante = Fabricante(cod, nome, cnpj, local)
        sql = f'insert into Fabricante (nome, cnpj, endereço) value ("{obj_fabricante.nome}","{obj_fabricante.cnpj}","{obj_fabricante.local}")'
        self.my_cursor.execute(sql) 
        self.conexao.commit()

    def listar(self, tabela):
        sql = f'select * from {tabela}'
        self.my_cursor.execute(sql) 
        lista = self.my_cursor.fetchall()
        for i in lista:
            print(i)
    
    def alterar_descricao(self, tabela, atributo, valor, cod):
        sql = f'update {tabela} set {atributo} = "{valor}" where cod = {cod}'
        self.my_cursor.execute(sql)
        self.conexao.commit()
    
    def deletar(self, tabela, cod): 
        sql = f'delete from {tabela} where cod = {cod}'
        self.my_cursor.execute(sql)
        self.conexao.commit()

    def nova(self):
        sql = f'select quantidade from Produto where cod = 1'
        self.my_cursor.execute(sql) 
        print(self.conexao)

