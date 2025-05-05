"""The file is responsible for fetching data from the database
"""
import pandas as pd

from app.config import ENGINE
from app.llm import generate_sql
from .schema_explorer import extract_sql_query

def execute_query(natural_language_query: str):
    """This function is responsible for fetching the data from the database

    Parameters
    ----------
    natural_language_query : str
        The question coming from the user

    Returns
    -------
    dict
        records
    """
    sql_query = generate_sql(natural_language_query)

    print(sql_query)
    sql_query = sql_query.strip()
    if sql_query.startswith("`") and sql_query.endswith("`"):
        sql_query = sql_query[1:-1]
    if sql_query.startswith("``sql") and sql_query.endswith("``"):
        sql_query = sql_query[5:-2]
    if sql_query.startswith("``") and sql_query.endswith("``"):
            sql_query = sql_query[2:-2]
    if "```sql" in sql_query.lower():
        sql_query = extract_sql_query(sql_query)
    print("after formatting ", sql_query)
    if any(x in sql_query for x in ["INSERT", "insert", "DELETE", "delete", "UPDATE", "update", "DROP", "drop", "ALTER", "alter"]):
         return {
                "message": "Failure. This section does not deal with modifiying data",
                "sql_query": sql_query
            }
    with ENGINE.connect() as conn:
        result = pd.read_sql(sql_query, conn)

    return result.to_dict(orient="records")
