from variables import *

#(target db, datawarehouse)
datawarehouse_db_config = {
    'username': 'postgres',
    'password': 'postgres',
    'database': '{}.format(datawarehouse_name)',
    'host': 'localhost',
    'autocommit' : True,
}

#(source db) 'postgres'
locations_db_config = {
    'username': 'postgres',
    'password': 'postgres',
    'database': 'locations',
    'host': 'localhost',
}

#(source db) 'postgres'
patrons_db_config = {
    'username': 'postgres',
    'password': 'postgres',
    'database': 'patrons',
    'host': 'localhost',
}

# (source db) 'postgres'
librarymanager_db_config = {
    'username': 'librarian',
    'password': '{}.format(librarian_password)',
    'database': 'librarymanager',
    'host': 'localhost',
}