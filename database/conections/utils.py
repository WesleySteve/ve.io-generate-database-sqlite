

def import_query(path, **kwargs):
    """Function to import query taking several arguments

    Args:
        path (os): path where the sql query is stored
        
    Returns:
        query: returns the result of the previous query
    """
    with open(path, "r", **kwargs) as file_query:
        query = file_query.read()
    return query



def execute_many_sql(sql, con):
    """Function that receives a sql connection and verbose (optional) and executes

    Args:
        sql (command): parameter that receive the query  
        con (parameter): conection string as database sqlite
    """

    for i in sql.split(";")[:-1]:
        con.execute(i)
        
