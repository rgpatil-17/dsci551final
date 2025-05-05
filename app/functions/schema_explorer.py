"""This file contains functions which are responsible for schema and database exploration
"""
import re 
from sqlalchemy import text
from app.config import ENGINE
from app.llm import generate_sql

def extract_sql_query(input_text, uri = 'sql'):
     match = re.search(rf"```{uri}\s*(.*?)\s*```", input_text, re.DOTALL | re.IGNORECASE)
     if match:
          return match.group(1).strip()
     return input_text

def explore_schema(user_question: str):
    """Get the details of the database/schema

    Parameters
    ----------
    user_question : str
        question from the user

    Returns
    -------
    str
        database/schema details
    """

    sql_query = generate_sql(user_question)
    print(sql_query)
    sql_query = sql_query.strip()
    if sql_query.startswith("`") and sql_query.endswith("`"):
        sql_query = sql_query[1:-1]
    if sql_query.startswith("``sql") and sql_query.endswith("``"):
        sql_query = sql_query[5:-2]
    if "```mysql" in sql_query.lower():
        sql_query = extract_sql_query(sql_query, 'mysql')
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
        result = conn.execute(text(sql_query))
        data = result.fetchall()

    print(data)
    return data
