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
)

