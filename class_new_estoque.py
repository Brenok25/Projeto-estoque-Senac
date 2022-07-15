from statistics import quantiles
import mysql.connector
from class_produto import *
from class_fabricante import *

class DBAestoque:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host= '127.0.0.1',
            user= 'root',
            password= 'Lucariobk25',
            database='estoque_senac'
        )

        self.my_cursor = self.conexao.cursor()
    
    def salva_produto(self, cod, nome, fabr):
        obj_produto = Produto(cod, nome, fabr)
        sql = f'insert into Produto (nome, fabricante) value ("{obj_produto.nome}", (select nome from Fabricante where cod = {fabr}))'
        # sql_1 = f'insert into Compra_venda (estoque) value (0)'
        self.my_cursor.execute(sql) 
        self.conexao.commit()
        # self.my_cursor.execute(sql_1) 
        # self.conexao.commit()
    

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
    
    def deletar(self, cod): 
        sql = f'delete from Produto where cod = {cod}'
        self.my_cursor.execute(sql)
        self.conexao.commit()