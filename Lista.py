def lista():
    janela=tk.Tk()
    
    janela.geometry("500x300") 
    janela.title("Tabelas")
    janela.title("Tabela Tkinter")

    colunas = ("Nome", "Idade", "Posição","Valor","Codigo")

    tree = ttk.Treeview(janela, columns=colunas, show='headings')

    tree.heading("Nome", text="Nome")
    tree.heading("Idade", text="Idade")
    tree.heading("Posição", text="Posição")
    tree.heading("Valor", text="valor")
    tree.heading("Codigo", text="Codigo")

    tree.column("Nome", width=100)
    tree.column("Idade", width=50)
    tree.column("Posição", width=100)
    tree.column("Valor", width=100)
    tree.column("Codigo", width=50)

    lista=AtletaBanco()
    dados = lista.get_all_atletas()

    for atleta in dados:
        tree.insert("", tk.END, values=(atleta.nome, atleta.idade, atleta.posicao, atleta.valor, atleta.cod))

    tree.pack()
