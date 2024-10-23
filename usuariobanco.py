import psycopg2 
from backend.Usuario import Usuario

class usuariobanco: 
    def __init__ (self):
        pass
    def pegarusuario(self, nome):

        
        conexao = psycopg2.connect (dbname = "20221214010037",
                                    user = "postgres",
                                    password = "270280",
                                    host = "localhost",
                                    port = 5432
                                    )

        cursor = conexao.cursor()
        codigo_sql = "SELECT * FROM Usuario WHERE nome = '"+ nome +"';"
        cursor.execute (codigo_sql)
        result = cursor.fetchone()
        conexao.commit()
        conexao.close()
        

        if result != None:
            nome =   result [0]
            senha =  result [1]
            codigo = result [2]
            usuario =Usuario(nome, senha, codigo)

        else: 
            usuario=None
        return usuario



