import os
import sqlalchemy



def create_db_sqlite(path, nome_banco):

    # define conection string as database sqlite
    str_conexao = "sqlite:///{path}"

    # loading dotenv
    str_conexao = str_conexao.format(path=os.path.join(path, nome_banco + ".db"))

    # creat conection as database sqlite
    con = sqlalchemy.create_engine(str_conexao)

    return con