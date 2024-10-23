class Produtos:
    def __init__ (self, nome, valor, banho,codigo,ativo=None):
        self.nome = nome
        self.valor = valor
        self.banho = banho
        self.ativo=ativo
        self.codigo = codigo
    def __str__(self):
        return f"Nome: {self.nome}\nValor:{self.valor}\nBanho:{self.banho}\nCódigo:{self.codigo}"

    