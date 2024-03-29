# python models
import sqlite3
from _pg import *
import pgdb

# variables
from variables import datawarehouse_name

# extract data from source db
def etl(query, source_conn, target_conn):
    source_cursor= source_conn.cursor()
    source_cursor.execute(query.select_query)
    data = source_cursor.fetchall()
    source_cursor.close()

    # if data load and commit data into warehouse; else return empty message
    if data:
        target_cursor = target_conn.cursor()
        target_cursor.executemany(query.load_query, data)
        target_conn.commit()
        print('Data succesfully loaded to warehouse db.')
        target_cursor.close()
    else:
        print('data is empty')

# establish connection with source database
def etl_process(queries, target_conn, source_db_config, db_platform):
    if db_platform == 'postgres':
        source_conn = pgdb.connect(**source_db_config)
    elif db_platform == 'sqlite3':
        source_conn = sqlite3.connect(**source_db_config)
    else: 
        return 'Error: db_platform not recognized.' 

    # loop through sql queries
    for query in queries:
        etl(query, source_conn, target_conn)
   
    #close source db connection
    source_conn.close()