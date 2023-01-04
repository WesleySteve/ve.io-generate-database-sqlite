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
  
  
def connect_db_sqlite(db_path):
    """Function to connect with local sqlite

    Returns:
        con: returns a connection sqlite database
    """

    # define connection string with sqlite database
    str_conexao = "sqlite:///{db_path}"

    str_conexao = "sqlite:///{path}".format(path=os.path.join(db_path))

    # create connection to sqlite database
    con = sqlalchemy.create_engine(str_conexao)

    return con
