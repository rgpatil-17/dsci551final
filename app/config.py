"""This file contains all the required configurations for the project
"""

from sqlalchemy import create_engine
from os import getenv

DB_NAME = getenv("DB_NAME")
DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")
URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
# change NBA_DB to older db when using data_modifier 

ENGINE = create_engine(URI)

#create an engine using uri. use the engine to connect to mysql database and execute queries 