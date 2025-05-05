"""This file contains the functions which are responsible for modifying the data
"""
from sqlalchemy import text
from app.config import ENGINE
from app.llm import generate_sql
from .schema_explorer import extract_sql_query

def modify_data(natural_language_command: str):
    """This function will modify the data in the database

    Parameters
    ----------
    natural_language_command : str
        The command coming from the user

    Returns
    -------
    dict
        success or failure message
    """

    try:
        sql_query = generate_sql(natural_language_command)
        print(sql_query)
        sql_query = sql_query.strip()
        if sql_query.startswith("`") and sql_query.endswith("`"):
            sql_query = sql_query[1:-1]
        if sql_query.startswith("``sql") and sql_query.endswith("``"):
            sql_query = sql_query[5:-2]
        if sql_query.startswith("``") and sql_query.endswith("``"):
            sql_query = sql_query[2:-2]
        if "```mysql" in sql_query.lower():
            sql_query = extract_sql_query(sql_query, 'mysql')
        # strip funciton removed white spaces start and end and removes back tape
        if "```sql" in sql_query.lower():
            sql_query = extract_sql_query(sql_query)
        print("after formatting ", sql_query) 
        if sql_query.startswith(("SELECT","DROP")):
            return {
                "message": "Failure. This section does not deal with reading data or dropping database",
                "sql_query": sql_query
            }
        
# if sql query starts with select then it will fail since this is data modifiter
        with ENGINE.connect() as conn:
            conn.execute(text(sql_query))
            conn.commit()

        return {"message": "Success", "sql_query": sql_query}
    except Exception as e:
        print(e)
        return {"message": "Failure", "sql_query": sql_query}
