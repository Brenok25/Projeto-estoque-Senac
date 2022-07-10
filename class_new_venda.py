from distutils.log import error
import mysql.connector
from class_historico import *
from class_produto import *

class Venda:

    def __init__(self):
        self.conexao = mysql.connector.connect(
            host= '127.0.0.1',
            user= 'root',
            password= 'Lucariobk25',
            database='estoque_senac'
        )

        self.my_cursor = self.conexao.cursor()
    
    def venda(self,cod,value,atributo):
        sql = f'update Compra_venda set {atributo} = "{value}" where cod = {cod} '
        sql_1 = f'update Compra_venda set final = (select (estoque - venda) where cod = {cod}) where cod = {cod};'
        sql_2 = f'update Compra_venda set estoque = (select final where cod = {cod}) where cod = {cod};'
        sql_3 = f'update Produto set quantidade = (select final from Compra_venda where cod = {cod}) where cod = {cod};'
        self.my_cursor.execute(sql) 
        self.conexao.commit()
        self.my_cursor.execute(sql_1) 
        self.conexao.commit()
        self.my_cursor.execute(sql_2) 
        self.conexao.commit()
        self.my_cursor.execute(sql_3) 
        self.conexao.commit()

        # Ta fazendo venda negativa

