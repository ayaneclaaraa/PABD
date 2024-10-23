import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.ProdutoBanco import Produtobanco



# Chamando a função para criar a tabela
def tela_tabela():
 
    janela = tk.Tk()
    janela.title("Loja Vivara")
    janela.geometry("500x300")
    label = tk.Label(janela,text="Produtos Disponíveis")
    label.pack(pady=30)

    colunas = ('nome', 'valor', 'banho', 'codigo')

    tabela = ttk.Treeview(janela, columns=colunas, show='headings')

    tabela.heading('nome', text='Nome')
    tabela.heading('valor', text='Valor')
    tabela.heading('banho', text='Banho')
    tabela.heading('codigo', text='Código')

    tabela.column('nome', width=100)
    tabela.column('valor', width=100)
    tabela.column('banho', width=100)
    tabela.column('codigo', width=100)

    pb=Produtobanco()
    dados=pb.pegarprodutos()


    for produto in dados:
        if produto.ativo==True:
            tabela.insert("", tk.END, values=(produto.nome, produto.valor, produto.banho, produto.codigo))

    tabela.pack(padx=10, pady=10)

    janela.mainloop()
    
def adicionar_produto():
    global entry_nome
    global entry_valor
    global entry_banho

    janela=tk.Tk()
    janela.geometry("500x300")
    janela.title("Loja vivara")

    label_nome=tk.Label(janela,text="Nome")
    label_nome.pack(pady=5)
    entry_nome=tk.Entry(janela)
    entry_nome.pack(pady=5)

    label_valor=tk.Label(janela,text="Valor")
    label_valor.pack(pady=5)
    entry_valor=tk.Entry(janela)
    entry_valor.pack(pady=5)
    


    label_banho=tk.Label(janela,text="Banho")
    label_banho.pack(pady=5)
    entry_banho=tk.Entry(janela)
    entry_banho.pack(pady=5)
    


    botao_criar=tk.Button(janela,text="Adicionar protduto",command=criar_produto)
    botao_criar.pack(pady=5)

    janela.mainloop()
def criar_produto(): 
    global entry_nome
    global entry_valor
    global entry_banho

    nome=entry_nome.get()
    valor=entry_valor.get()
    banho=entry_banho.get()
    status='true'

    pb=Produtobanco()  

    try:
        criar=pb.criar_produto(nome,valor,banho,status)
        messagebox.showinfo("compra","Produto adicionado com sucesso!")
    except:
        messagebox.showerror("erro","Impossivel realizar compra")

def remover_produto():
    global entry_cod
    janela = tk.Tk()
    janela.title("Loja Vivara")

    janela.geometry("500x300")

    label = tk.Label(janela,text="Digite o codigo do produto que você quer vender")
    label.pack(pady=5)

    entry_cod = tk.Entry(janela)
    entry_cod.pack(pady=5)

    botao_vender = tk.Button(janela,text="vender",command=vender)
    botao_vender.pack(pady=5)
    janela.mainloop()
def vender():
    global entry_cod
    
    cod=entry_cod.get()

    pb=Produtobanco()
    try:
        venda=pb.update_produto_to_false(cod)
        messagebox.showinfo("venda","produto vendido com sucesso")
    except:
        messagebox.showerror("erro","impossivel vender produto")


def atualizar_produto():
    global entry_nome
    global entry_valor
    global entry_banho
    global entry_cod

    janela=tk.Tk()
    janela.geometry("500x300")
    janela.title("Loja vivara")

    label_cod=tk.Label(janela,text="digite o codigo do produto que você quer atualizar")
    label_cod.pack(pady=5)

    entry_cod=tk.Entry(janela)
    entry_cod.pack(pady=5)

    label_nome=tk.Label(janela,text="Nome")
    label_nome.pack(pady=5)
    entry_nome=tk.Entry(janela)
    entry_nome.pack(pady=5)

    label_valor=tk.Label(janela,text="Valor")
    label_valor.pack(pady=5)
    entry_valor=tk.Entry(janela)
    entry_valor.pack(pady=5)
    


    label_banho=tk.Label(janela,text="Banho")
    label_banho.pack(pady=5)
    entry_banho=tk.Entry(janela)
    entry_banho.pack(pady=5)
    

    botao_atualizar=tk.Button(janela,text="atualizar protduto",command=atualizar)
    botao_atualizar.pack(pady=5)

    janela.mainloop()

def atualizar():
    global entry_nome
    global entry_valor
    global entry_banho
    global entry_cod

    nome=entry_nome.get()
    valor=entry_valor.get()
    banho=entry_banho.get()
    cod=entry_cod.get()

    pb=Produtobanco()
    try:
        atualizar=pb.atualizar_produto(cod,nome,banho,valor)
        messagebox.showinfo("certo","produto atualizado")
    except:
        messagebox.showerror("erro","produto não")


def run():
    janela = tk.Tk()
    janela.title("Loja Vivara")

    janela.geometry("500x300")

    label = tk.Label(janela,text="VIVARA")
    label.pack(pady=30)

    botao_lista = tk.Button(janela,text = "Produtos:",command=tela_tabela)
    botao_lista.pack(pady=10)

    botao_add = tk.Button(janela,text = "Adicionar produto",command=adicionar_produto)
    botao_add.pack(pady=10)

    botao_remover = tk.Button(janela,text = "vender produto",command=remover_produto)
    botao_remover.pack(pady=10)

    botao_atualizar=tk.Button(janela,text = "atualizar produto",command=atualizar_produto)
    botao_atualizar.pack(pady=10)

    janela.mainloop()
