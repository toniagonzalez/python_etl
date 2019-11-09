from variables import datawarehouse_name

#(target db, datawarehouse)
datawarehouse_db_config = {
    'username': 'postgres',
    'password': 'postgres',
    'database': '{}.format(datawarehouse_name)',
    'host': 'localhost',
    'autocommit' : True,
}

#(source db) postgres
first_db_config = {
    'username': 'postgres',
    'password': 'postgres',
    'database': '',
    'host': 'localhost',
}

#(source db)
second_db_config = {
    'username': 'postgres',
    'password': 'postgres',
    'database': '',
    'host': 'localhost',
}

# (source db)
third_db_config = {
    'username': 'sqlite3',
    'password': 'sqlite3',
    'database': '',
    'host': '',
}