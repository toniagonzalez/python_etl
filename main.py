# variables
from db_credentials import datawarehouse_db_config, source1_db_config, source2_db_config, source3_db_config
from sql_queries import source1_db_queries, source2_db_queries, source3_db_queries
from variables import source1_name, source2_name, source3_name
import pgdb

# methods
from etl import etl_process


def main():
    print('Starting etl..')

    #establish connnection to target db
    target_conn = pgdb.connect(**datawarehouse_db_config)

    #loop through credentials for each source db
    # locations db
    for config in source1_db_config:
        try:
            print('Loading db: {}'.format(source1_name))
            etl_process(source1_db_queries, target_conn, config, 'postgres')
        except Exception as error:
            print('etl for {} has error'.format(source1_name))
            print('Error message: {}'.format(error))
            continue
      
   # patrons db
    for config in source2_db_config:
        try:
            print('Loading db: {}'.format(source2_name))
            etl_process(source2_db_queries, target_conn, config, 'postgres')
        except Exception as error:
            print('etl for {} has error'.format(source2_name))
            print('Error message: {}'.format(error))
            continue
    
    # librarymanager db
    for config in source3_db_config:
        try:
            print('Loading db: {}'.format(source3_name))
            etl_process(source3_db_queries, target_conn, config, 'postgres')
        except Exception as error:
            print('etl for {} has error'.format(source3_name))
            print('Error message: {}'.format(error))
            continue

    target_conn.close()

if __name__=="__main__":
    main()