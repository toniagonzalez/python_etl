# variables
from db_credentials import datawarehouse_db_config, locations_db_config, patrons_db_config, librarymanager_db_config
from sql_queries import locations_db_queries, patrons_db_queries, librarymanager_db_queries
import pgdb

# methods
from etl import etl_process


def main():
    print('Starting etl..')

    #establish connnection to target db
    target_conn = pgdb.connect(**datawarehouse_db_config)

    #loop through credentials for each source db
    # locations db
    for config in locations_db_config:
        try:
            print("Loading db: ")
            etl_process(locations_db_queries, target_conn, config, 'postgres')
        except Exception as error:
            print("etl for {} has error".format(config))
            print('Error message: {}'.format(error))
            continue
      
   # patrons db
    for config in patrons_db_config:
        try:
            print("Loading db: ")
            etl_process(patrons_db_queries, target_conn, config, 'postgres')
        except Exception as error:
            print("etl for {} has error".format(config))
            print('Error message: {}'.format(error))
            continue
    
    # librarymanager db
    for config in librarymanager_db_config:
        try:
            print("Loading db: ")
            etl_process(librarymanager_db_queries, target_conn, config, 'postgres')
        except Exception as error:
            print("etl for {} has error".format(config))
            print('Error message: {}'.format(error))
            continue

    target_conn.close()

if __name__=="__main__":
    main()