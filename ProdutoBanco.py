import psycopg2 
from backend.Produtos import Produtos

class Produtobanco: 
    def __init__ (self):
        self.conexao=psycopg2.connect(dbname="20221214010037",user="postgres",password="270280",host="localhost",port=5432)
        self.cursor=self.conexao.cursor()
        self.conexao.autocommit=True
    def pegarprodutos(self):
        codigo_sql="SELECT * FROM produtos"
        self.cursor.execute(codigo_sql)
        result=self.cursor.fetchall()
        listaprodutos=[]

        if result !=None:
            for produto in result:
                nome=produto[0]
                valor=produto[1]
                banho=produto[2]
                ativo=produto[3]
                codigo=produto[4]
                produto=Produtos(nome,valor,banho,codigo,ativo)
                listaprodutos.append(produto)

        else:
            listaprodutos=None
        return listaprodutos

    def criar_produto(self,nome,valor,banho,ativo):

        codigo_sql=f"INSERT INTO produtos(nome,valor,banho,ativo) VALUES ('{nome}',{valor},'{banho}','{ativo}')"
        self.cursor.execute(codigo_sql)

    def update_produto_to_false(self,cod):
        codigo_sql=f"UPDATE produtos SET ativo='false' WHERE codigo={cod}"
        self.cursor.execute(codigo_sql)

    def atualizar_produto(self,cod,nome,banho,valor):
        codigo_sql=f"UPDATE produtos SET nome='{nome}', valor={valor}, banho='{banho}' WHERE codigo={cod}"
        self.cursor.execute(codigo_sql)
