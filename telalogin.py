import tkinter as tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.usuariobanco import usuariobanco
from Frontend.TelaHome import run


def validar_login():
    
    nome_usuario = entrada_usuario.get()
    senha_usuario = senha.get()

    usuario_banco = usuariobanco()
    usuario=usuario_banco.pegarusuario(nome_usuario)

    if usuario != None and usuario.senha.strip() == senha_usuario:
        run()
    else:
        messagebox.showerror("Erro", "nome ou senha inválidos")

janela = tk.Tk()


janela.title("Tela de Login")
janela.geometry("500x300")
texto = tk.Label (janela, text= "Bem vindo a loja vivara")
texto.pack(pady=5)
label_usuario = tk.Label(janela, text="Nome:")
label_usuario.pack(pady=5)
entrada_usuario = tk.Entry(janela)
entrada_usuario.pack(pady=5)

label_senha = tk.Label(janela, text="Senha:")
label_senha.pack(pady=5)

senha=tk.Entry(janela,show='*')
senha.pack(pady=5)

botao_login = tk.Button(janela, text="Login", command=validar_login)
botao_login.pack(pady=20)

janela.mainloop()
