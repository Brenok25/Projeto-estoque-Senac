
from class_estoque import *
from class_historico import *
import mysql.connector

class Venda:

    def __init__(self):
        self.conexao = mysql.connector.connect(
            host= '127.0.0.1',
            user= 'root',
            password= 'Lucariobk25',
            database='estoque_senac'
        )

        self.my_cursor = self.conexao.cursor()
    
    def vender(self,cod,value):
        sql = f'insert into Compra (qunt, comprado) value (100,"{value}")where cod = "{cod}"'
        self.my_cursor.execute(sql) 
        self.conexao.commit()

