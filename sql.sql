drop database estoque_senac;
create database estoque_senac;
use estoque_senac;


create table Produto(
cod int auto_increment,
nome varchar(40),
fabricante varchar(40),
quantidade int,
primary key (cod)
);

create table Fabricante(
cod int auto_increment,
nome varchar(40),
cnpj int,
endereço varchar(40),
primary key (cod)
);

create table Compra_venda(
cod int auto_increment,
estoque int, # O q tem no estoque
compra int, # Valor comprado
venda int,
final int, # Valor atualizado
primary key (cod)
);

#create table Venda(
#cod int auto_increment,
#estoque int, # O q tem no estoque
#venda int, # Valor vendido
#final int, # Valor atualizado
#primary key (cod)
#);



#insert into Compra (estoque,compra) value(100,100);
select * From Compra_venda;
select * From Produto;
#select sum(comprado) from Compra where cod = 1;
#update Compra set comprado = sum(cod + quant) where cod = 1;
#select (estoque + compra) from Compra where cod = 2;
#update  Compra set final = (select (estoque + compra) where cod = 2) where cod = 2;
#update Produto set quantidade = (select final from Compra where cod = 2) where cod = 2;

#insert into Compra_venda (estoque,venda) value(100,50);
#update  Compra_venda set final = (select (estoque - venda) where cod = 1) where cod = 1;
#update Produto set quantidade = (select final from Compra_venda where cod = 1) where cod = 1;
