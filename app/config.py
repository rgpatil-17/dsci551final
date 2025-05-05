"""This file contains all the required configurations for the project
"""

from sqlalchemy import create_engine

DB_NAME = "NBA_DB"

URI = f"mysql+pymysql://root:@127.0.0.1:3306/{DB_NAME}"
# change NBA_DB to older db when using data_modifier 

ENGINE = create_engine(URI)

#create an engine using uri. use the engine to connect to mysql database and execute queries 