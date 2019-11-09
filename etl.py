# python models
import sqlite3
import psycopg2

# variables
from variables import datawarehouse_name

# extract data from source db
def etl(query, source_conn, target_conn):
    source_cursor= source_conn.cursor()
    source_cursor.execute(query.select_query)
    data = source_cursor.fetchall()
    source_cursor.close()

    # if data  load into warehouse else return empty message
    if data:
        target_cursor = target_conn.cursor()
        target_cursor.execute("USE {}".format(datawarehouse_name))
        target_cursor.executemany(query.load_query, data)
        print('Data succesfully loaded to warhouse db.')
        target_cursor.close()
    else:
        print('data is empty')

# establish connection with source database
def etl_process(queries, target_conn, source_db_config, db_platform):
    if db_platform == 'postgres':
        source = psycopg2.connect(**source_db_config) 
    elif db_platform == 'sqlite3':
        source = sqlite3.connect(**source_db_config)
    else: 
        return 'Error: db_platform not recognized.' 

    # loop through sql queries
    for query in queries:
        etl(query, source_conn, target_conn)

    #close source db connection
    source_conn.close()