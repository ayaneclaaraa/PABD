class Usuario: 
    def __init__(self, nome, senha, codigo):
        self.nome = nome
        self.senha = senha
        self.codigo = codigo

    def __str__(self):
        return f'nome: {self.nome}\nsenha: {self.senha}\ncodigo: {self.codigo}'
