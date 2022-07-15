from tkinter import *
from turtle import left

from mysqlx import Row
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

def remove(button):
    button.grid_remove()


fr0 = LabelFrame (root).grid()

produto = Button(fr0, text="Produto", command= lambda: [remove(produto),remove(fabr), fr1.grid(row=0,column=0)])
produto.grid(row=0, column=0)

fabr = Button(fr0, text='Fabricante', command= lambda: [remove(produto),remove(fabr), fr1.grid(row=0,column=0)])
fabr.grid(row=0, column=1)

# Produto
fr1 = LabelFrame(root)

cadastrar_pr = Button(fr1, text="Cadasstrar Produto", command= lambda: [fr1.grid_remove(), fr1_1.grid(row=0,column=0)])
cadastrar_pr.grid(row=0, column=0)

delete_pr = Button(fr1, text='Deletar Produto', command= lambda: [fr1.grid_remove(), fr1_2.grid(row=0,column=0)])
delete_pr.grid(row=0, column=1)

listar_fr1 = Button(fr1, text='listar', command= lambda: [fr1.grid_remove(), fr1_3.grid(row=0,column=0)])
listar_fr1.grid(row=0, column=2)

voltar = Button(fr1, text='voltar', command= lambda: [fr1.grid_remove(), fr1.grid(row=0,column=0)])
voltar.grid(row=0, column=3)

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

lb1_fr1_3 = Label(fr1_3, text='')
lb2_fr1_3 = Label(fr1_3, text='')

confirm_fr1_3 = Button(fr1_3, text="Listar Produtos ", command= deletar )
confirm_fr1_3.grid()

voltar_fr1_3 = Button(fr1_3, text='voltar', command= lambda: [fr1_3.grid_remove(),fr1.grid(row=0,column=0)])
voltar_fr1_3.grid()





























# fr0 = LabelFrame (root).grid(row=0,column=0)

# cadastrar_produto = Button(fr0, text="Cadastrar Produto", command= lambda: [remove(cadastrar_produto),remove(cadastrar_fabr), fr1.grid(row=0,column=0)])
# cadastrar_produto.grid(row=0, column=0, padx=100, pady=80)
# cadastrar_fabr = Button(fr0, text="Cadastrar Produto")
# cadastrar_fabr.grid(row=0, column=1)

# fr1 = LabelFrame (root)

# voltar = Button(fr1, text="voltar").grid()

# fr2 = LabelFrame (root)

# voltar = Button(fr2, text="voltar").grid()



root.mainloop()

    


