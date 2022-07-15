    
from tkinter import *
from class_new_estoque import *

root = Tk()
root.title('Estoque')
root.geometry('500x300')
root.config(background='#00c')
estoque = DBAestoque()

def noCommand():
    print('oi')

def new_produto():
    fr1 = Tk()
    fr1.title('Cadastrar Produto')
    fr1.geometry('500x300')
    fr1.config(background='#ff0')

    def cadastro_produto():
        cod = None
        nome = nome_fr1.get()
        fabr = fabr_fr1.get()
        estoque.salva_produto(cod,nome,fabr)

    title = Label(fr1, text= "Cadastre um novo produto", bg="#ff0", font="roboto 15").pack()
    label = Label(fr1, text= "Digite o nome do produto",bg="#ff0", font="roboto 10" ).pack()
    nome_fr1 = Entry(fr1, font="roboto 10", textvariable='var' ).pack()

    label2 = Label(fr1, text= "Digite nome do Fabricante",bg="#ff0", font="roboto 10" ).pack()
    fabr_fr1 = Entry(fr1, font="roboto 10" ).pack()

    confirmar = Button(fr1, text="Cadastrar", command= lambda: cadastro_produto()).pack()
    alert = Label(fr1, text="", bg='#ff0').pack()
    voltar = Button(fr1, text="voltar", command=fr1.destroy).pack()

    fr1.mainloop()

def new_fabr():
    fr1_fbr = Tk()
    fr1_fbr.title('Cadastrar Fabricante')
    fr1_fbr.geometry('500x300')
    fr1_fbr.config(background='#ff0')

    def cadastro_produto():
        cod = None
        nome = nome_fr1_fbr.get()
        cnpj = cnpj_fr1_fbr.get()
        local = local_fr1_fbr.get()
        estoque.salva_produto(cod,nome,cnpj,local)

    title = Label(fr1_fbr, text= "Cadastre um novo Fabricante", bg="#ff0", font="roboto 15").pack()
    label = Label(fr1_fbr, text= "Digite o nome do Fabricante",bg="#ff0", font="roboto 10" ).pack()
    nome_fr1_fbr = Entry(fr1_fbr, font="roboto 10" ).pack()

    label = Label(fr1_fbr, text= "Digite o CNPJ do Fabricante",bg="#ff0", font="roboto 10" ).pack()
    cnpj_fr1_fbr = Entry(fr1_fbr, font="roboto 10" ).pack()

    label = Label(fr1_fbr, text= "Digite o endereço do Fabricante",bg="#ff0", font="roboto 10" ).pack()
    local_fr1_fbr = Entry(fr1_fbr, font="roboto 10" ).pack()

    confirmar = Button(fr1_fbr, text="Cadastrar").pack()
    voltar = Button(fr1_fbr, text="voltar", command=fr1_fbr.destroy).pack()

    fr1_fbr.mainloop()

def list_produto():
    fr2 = Tk()
    fr2.title('listar Produto')
    fr2.geometry('500x300')
    fr2.config(background='#00ed00')
    title = Label(fr2, text= "Listar produtos", bg="#00ed00", font="roboto 15").pack()
    voltar = Button(fr2, text="voltar", command=fr2.destroy).pack()


    fr2.mainloop()
    

def list_fabr():
    fr2_fabr = Tk()
    fr2_fabr.title('listar Produto')
    fr2_fabr.geometry('500x300')
    fr2_fabr.config(background='#00ed00')
    title = Label(fr2_fabr, text= "Listar fabricantes", bg="#00ed00", font="roboto 15").pack()
    voltar = Button(fr2_fabr, text="voltar", command=fr2_fabr.destroy).pack()


    fr2_fabr.mainloop()
    

def delete_produto():
    fr3 = Tk()
    fr3.title('deletar Produto')
    fr3.geometry('500x300')
    fr3.config(background='#0ed')
    title = Label(fr3, text= "Delete um produto", bg="#0ed", font="roboto 15").pack()
    label = Label(fr3, text= "Digite o código do produto",bg="#0ed", font="roboto 10" ).pack()
    nome = Entry(fr3, font="roboto 10" ).pack()

    label2 = Label(fr3, text= "Digite nome do produto",bg="#0ed", font="roboto 10" ).pack()
    fabr = Entry(fr3, font="roboto 10" ).pack()

    confirmar = Button(fr3, text="Deletar ").pack()
    voltar = Button(fr3, text="voltar", command=fr3.destroy).pack()

    fr3.mainloop()

def delete_fabr():
    fr3_fabr = Tk()
    fr3_fabr.title('deletar Gabricante')
    fr3_fabr.geometry('500x300')
    fr3_fabr.config(background='#0ed')
    title = Label(fr3_fabr, text= "Delete um Fabricante", bg="#0ed", font="roboto 15").pack()
    label = Label(fr3_fabr, text= "Digite o código do Fabricante",bg="#0ed", font="roboto 10" ).pack()
    nome = Entry(fr3_fabr, font="roboto 10" ).pack()

    label2 = Label(fr3_fabr, text= "Digite nome do Fabricante",bg="#0ed", font="roboto 10" ).pack()
    fabr = Entry(fr3_fabr, font="roboto 10" ).pack()

    confirmar = Button(fr3_fabr, text="Deletar").pack()
    voltar = Button(fr3_fabr, text="voltar", command=fr3_fabr.destroy).pack()

    fr3_fabr.mainloop()


barraMenu = Menu(root)

menuHome = Menu(barraMenu, tearoff=0)
menuHome.add_command(label="Novo", command= new_produto)
menuHome.add_command(label="listar", command= list_produto)
menuHome.add_command(label="Deletar", command= delete_produto)
menuHome.add_separator()
menuHome.add_command(label="Sair", command= root.quit)
barraMenu.add_cascade(label= "Produto", menu =menuHome )
root.config(menu= barraMenu)

menuHome = Menu(barraMenu, tearoff=0)
menuHome.add_command(label="Novo", command= new_fabr)
menuHome.add_command(label="listar", command= list_fabr)
menuHome.add_command(label="Deletar", command= delete_fabr)
menuHome.add_separator()
menuHome.add_command(label="Sair", command= root.quit)
barraMenu.add_cascade(label= "Fabricante", menu =menuHome )
root.config(menu= barraMenu)

menuHome = Menu(barraMenu, tearoff=0)
menuHome.add_command(label="Compra", command= noCommand)
menuHome.add_command(label="Venda", command= noCommand)
menuHome.add_separator()
menuHome.add_command(label="Sair", command= root.quit)
barraMenu.add_cascade(label= "Movimentação", menu =menuHome )
root.config(menu= barraMenu)


title = Label(root, text= "Bem vindo ao Estoque", bg="#00c", font="roboto 15", fg="#fff").pack(pady = 100)



root.mainloop()

    


