from tkinter import *
from class_new_estoque import *

root = Tk()
root.title('Estoque')
root.geometry('500x300')
root.config(background='#00c')
estoque = DBAestoque()

def salvarProduto():
    cod = None
    nome = ent1_fr1_1.get()
    fabr = ent2_fr1_1.get()
    estoque.salva_produto(cod, nome, fabr)

def deletar():
    cod = ent1_fr1_2.get()
    estoque.deletar(cod)

def listar_produtos():
    tabela = 'Produto'
    list1= estoque.listar(tabela)
    for i in list1:
        lb2_fr1_3['text'] += 'Cod: ' + str(i[0]) + ' ' + 'Prod: ' +str(i[1]) + '\n'
    return list1

def alterar():
    tabela = 'Produto'
    atributo = 'nome'
    cod = in0_fr1_4.get()
    valor = in1_fr1_4.get()
    estoque.alterar_descricao(tabela, atributo, valor, cod)

def salvarFabricante() :
    cod = None
    nome = ent1_fr2_1.get()
    cnpj = ent2_fr2_1.get()
    local = ent3_fr2_1.get()
    estoque.salva_fabricante(cod, nome, cnpj, local)

def deletar_fabri():
    cod = ent1_fr2_2.get()
    estoque.deletar_fabr(cod)

def listar_fabr():
    atributo = 'Fabricante'
    list1= estoque.listar(atributo)
    for i in list1:
        lb2_fr2_3['text'] += 'Cod: ' + str(i[0]) + ' ' + 'Fab: ' + str(i[1]) + '\n'
    return list1


def alterar_fabr():
    tabela = 'Fabricante'
    atributo = 'nome'
    cod = in0_fr2_4.get()
    valor = in1_fr2_4.get()
    estoque.alterar_descricao(tabela, atributo, valor, cod)


def remove(button):
    button.grid_remove()


fr0 = LabelFrame (root).grid()

produto = Button(fr0, text="Produto", command= lambda: [remove(produto),remove(fabr), fr1.grid(row=0,column=0)])
produto.grid(row=0, column=0)

fabr = Button(fr0, text='Fabricante', command= lambda: [remove(produto),remove(fabr), fr2.grid(row=0,column=0)])
fabr.grid(row=0, column=1)

# Produto
fr1 = LabelFrame(root)

cadastrar_pr = Button(fr1, text="Cadasstrar Produto", command= lambda: [fr1.grid_remove(), fr1_1.grid(row=0,column=0)])
cadastrar_pr.grid(row=0, column=0)

delete_pr = Button(fr1, text='Deletar Produto', command= lambda: [fr1.grid_remove(), fr1_2.grid(row=0,column=0)])
delete_pr.grid(row=0, column=1)

listar_fr1 = Button(fr1, text='listar', command= lambda: [fr1.grid_remove(), fr1_3.grid(row=0,column=0)])
listar_fr1.grid(row=0, column=2)

alterar_fr1 = Button(fr1, text='Alterar', command= lambda: [fr1.grid_remove(), fr1_4.grid(row=0,column=0)])
alterar_fr1.grid(row=0, column=3)

voltar = Button(fr1, text='voltar', command= lambda: [fr1.grid_remove(), fr1.grid(row=0,column=0)])
voltar.grid(row=0, column=4)

# Cadastrar Produto
fr1_1 = LabelFrame(root)
lb1_fr1_1 = Label(fr1_1, text='Cadastrar Produto')
lb1_fr1_1.grid()

lb2_fr1_1 = Label(fr1_1, text='Nome do Produto ')
lb2_fr1_1.grid()

ent1_fr1_1 = Entry(fr1_1, text='') #produto
ent1_fr1_1.grid()

lb3_fr1_1 = Label(fr1_1, text='Cod do Fabricante: ')
lb3_fr1_1.grid()
ent2_fr1_1 = Entry(fr1_1, text='')# ID
ent2_fr1_1.grid()

confirm_fr1_1 = Button(fr1_1, text="Cadasstrar ", command= salvarProduto )
confirm_fr1_1.grid()

voltar_fr1_1 = Button(fr1_1, text='voltar', command= lambda: [fr1_1.grid_remove(),fr1.grid(row=0,column=0)])
voltar_fr1_1.grid()

# Deletar Produto
fr1_2 = LabelFrame(root)
lb1_fr1_2 = Label(fr1_2, text='Deletar Produto')
lb1_fr1_2.grid()

lb2_fr1_2 = Label(fr1_2, text='Cod do Produto: ')
lb2_fr1_2.grid()
ent1_fr1_2 = Entry(fr1_2, text='')# ID
ent1_fr1_2.grid()

confirm_fr1_2 = Button(fr1_2, text="Deletar ", command= deletar )
confirm_fr1_2.grid()

voltar_fr1_2 = Button(fr1_2, text='voltar', command= lambda: [fr1_2.grid_remove(),fr1.grid(row=0,column=0)])
voltar_fr1_2.grid()


# Listar Produto
fr1_3 = LabelFrame(root)
lb1_fr1_3 = Label(fr1_3, text='Listar Produtos')
lb1_fr1_3.grid()

lb2_fr1_3 = Label(fr1_3, text='')
lb2_fr1_3.grid()

confirm_fr1_3 = Button(fr1_3, text="Listar Produtos ", command= listar_produtos )
confirm_fr1_3.grid()

voltar_fr1_3 = Button(fr1_3, text='voltar', command= lambda: [fr1_3.grid_remove(),fr1.grid(row=0,column=0)])
voltar_fr1_3.grid()

# Alterar Produto
fr1_4 = LabelFrame(root)
lb1_fr1_4 = Label(fr1_4, text='Alterar Produtos')
lb1_fr1_4.grid()

lb2_fr1_4= Label(fr1_4, text='Insira o Cod')
lb2_fr1_4.grid()

in0_fr1_4 = Entry(fr1_4, text='')# ID
in0_fr1_4.grid()

lb3_fr1_4 = Label(fr1_4, text='Insira um novo nome: ')
lb3_fr1_4.grid()
in1_fr1_4 = Entry(fr1_4, text='')
in1_fr1_4.grid()

confirm_fr1_4 = Button(fr1_4, text="Alterar Nome ", command= alterar )
confirm_fr1_4.grid()

voltar_fr1_4 = Button(fr1_4, text='voltar', command= lambda: [fr1_4.grid_remove(),fr1.grid(row=0,column=0)])
voltar_fr1_4.grid()


fr2 = LabelFrame(root)

# Fabricante
fr2 = LabelFrame(root)

cadastrar_pr = Button(fr2, text="Cadastrar Fabricante", command= lambda: [fr2.grid_remove(), fr2_1.grid(row=0,column=0)])
cadastrar_pr.grid(row=0, column=0)

delete_pr = Button(fr2, text='Deletar Fabricante', command= lambda: [fr2.grid_remove(), fr2_2.grid(row=0,column=0)])
delete_pr.grid(row=0, column=1)

listar_fr1 = Button(fr2, text='listar', command= lambda: [fr2.grid_remove(), fr2_3.grid(row=0,column=0)])
listar_fr1.grid(row=0, column=2)

alterar_fr1 = Button(fr2, text='Alterar', command= lambda: [fr2.grid_remove(), fr2_4.grid(row=0,column=0)])
alterar_fr1.grid(row=0, column=3)

voltar = Button(fr2, text='voltar', command= lambda: [fr2.grid_remove(), fr2.grid(row=0,column=0)])
voltar.grid(row=0, column=4)


# Cadastrar Fabricante
fr2_1 = LabelFrame(root)
lb1_fr2_1 = Label(fr2_1, text='Cadastrar Fabricante')
lb1_fr2_1.grid()

lb2_fr2_1 = Label(fr2_1, text='Nome do Fabricante ')
lb2_fr2_1.grid()
ent1_fr2_1 = Entry(fr2_1, text='') #fabricante
ent1_fr2_1.grid()

lb3_fr2_1 = Label(fr2_1, text='CNPJ do Fabricante: ')
lb3_fr2_1.grid()
ent2_fr2_1 = Entry(fr2_1, text='')# CNPJ
ent2_fr2_1.grid()

lb4_fr2_1 = Label(fr2_1, text='Endereço do Fabricante: ')
lb4_fr2_1.grid()
ent3_fr2_1 = Entry(fr2_1, text='')# local
ent3_fr2_1.grid()

confirm_fr2_1 = Button(fr2_1, text="Cadastrar ", command= salvarFabricante )
confirm_fr2_1.grid()

voltar_fr2_1 = Button(fr2_1, text='voltar', command= lambda: [fr2_1.grid_remove(),fr2.grid(row=0,column=0)])
voltar_fr2_1.grid()


# Deletar Fabricante
fr2_2 = LabelFrame(root)
lb1_fr2_2 = Label(fr2_2, text='Deletar Fabricante')
lb1_fr2_2.grid()

lb2_fr2_2 = Label(fr2_2, text='Cod do Fabricante: ')
lb2_fr2_2.grid()
ent1_fr2_2 = Entry(fr2_2, text='')# ID
ent1_fr2_2.grid()

confirm_fr2_2 = Button(fr2_2, text="Deletar ", command= deletar_fabri )
confirm_fr2_2.grid()

voltar_fr2_2 = Button(fr2_2, text='voltar', command= lambda: [fr2_2.grid_remove(),fr2.grid(row=0,column=0)])
voltar_fr2_2.grid()



# Listar Fabricante
fr2_3 = LabelFrame(root)
lb2_fr1_3 = Label(fr2_3, text='Listar Fabricante')
lb2_fr1_3.grid()

lb2_fr2_3 = Label(fr2_3, text='')
lb2_fr2_3.grid()

confirm_fr2_3 = Button(fr2_3, text="Listar  ", command= listar_fabr )
confirm_fr2_3.grid()

voltar_fr2_3 = Button(fr2_3, text='voltar', command= lambda: [fr2_3.grid_remove(),fr2.grid(row=0,column=0)])
voltar_fr2_3.grid()


# Alterar Fabricante
fr2_4 = LabelFrame(root)
lb1_fr2_4 = Label(fr2_4, text='Alterar Fabricantea')
lb1_fr2_4.grid()

lb2_fr2_4= Label(fr2_4, text='Insira o Cod')
lb2_fr2_4.grid()

in0_fr2_4 = Entry(fr2_4, text='')# ID
in0_fr2_4.grid()

lb3_fr2_4 = Label(fr2_4, text='Insira um novo nome: ')
lb3_fr2_4.grid()
in1_fr2_4 = Entry(fr2_4, text='')
in1_fr2_4.grid()

confirm_fr2_4 = Button(fr2_4, text="Alterar Nome ", command= alterar_fabr )
confirm_fr2_4.grid()

voltar_fr2_4 = Button(fr2_4, text='voltar', command= lambda: [fr2_4.grid_remove(),fr2.grid(row=0,column=0)])
voltar_fr2_4.grid()

root.mainloop()
