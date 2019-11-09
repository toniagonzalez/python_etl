# variables
from db_credentials import datawarehouse_db_config, first_db_config, second_db_config, third_db_config
from sql_queries import first_db_queries, second_db_queries, third_db_queries
from variables import *

# methods
from etl import etl_process


def main():
    print('Starting etl..')

    #establish connnection to target db
    target_conn = psycodb.connect(datawarehouse_db_config)

    #loop through credentials
    # first db
    for config in first_db_config:
        try:
            print("Loading db: " + config['database'])
            etl_process(first_db_queries, target_conn, config, 'db_platform')
        except Exception as error:
            print("etl for {} has error".format(config['database']))
            print('Error message: {}'.format(error))
            continue
      
   # second db
    for config in second_db_config:
        try:
            print("Loading db: " + config['database'])
            etl_process(first_db_queries, target_conn, config, 'db_platform')
        except Exception as error:
            print("etl for {} has error".format(config['database']))
            print('Error message: {}'.format(error))
            continue
    
    # third db
    for config in third_db_config:
        try:
            print("Loading db: " + config['database'])
            etl_process(first_db_queries, target_conn, config, 'db_platform')
        except Exception as error:
            print("etl for {} has error".format(config['database']))
            print('Error message: {}'.format(error))
            continue

    target_conn.close()

    if __name__=="__main__":
        main()