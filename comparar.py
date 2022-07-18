# Listar Produto
fr1_3 = LabelFrame(root)
lb1_fr1_3 = Label(fr1_3, text='Listar Produtos')
lb1_fr1_3.grid()

lb2_fr1_3 = Label(fr1_3, text='')
lb2_fr1_3.grid()

confirm_fr1_3 = Button(fr1_3, text="Listar Produtos ", command= listar_pdr )
confirm_fr1_3.grid()

voltar_fr1_3 = Button(fr1_3, text='voltar', command= lambda: [fr1_3.grid_remove(),fr1.grid(row=0,column=0)])
voltar_fr1_3.grid()


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