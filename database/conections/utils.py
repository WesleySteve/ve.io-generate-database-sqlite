

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
