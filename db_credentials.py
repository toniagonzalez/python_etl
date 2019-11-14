from variables import datawarehouse_name

#(target db, datawarehouse)
datawarehouse_db_config = {
    'dbname': '{}'.format(datawarehouse_name),
    'host': 'localhost',
    'port': '5432',
    'user': 'toniagonzalez',
    'password': '',
}

#(source db) 'postgres'
locations_db_config = [
    {
        'dbname': 'locations',
        'host': 'localhost',
        'port': '5432',
        'user': 'toniagonzalez',
        'password': '',
    }
]

#(source db) 'postgres'
patrons_db_config = [
    {
        'dbname': 'patrons',
        'host': 'localhost',
        'port': '5432',
        'user': 'toniagonzalez',
        'password': '',
    }
]

# (source db) 'postgres'
librarymanager_db_config = [
    {
        'dbname': 'librarymanager',
        'host': 'localhost',
        'port': '5432',
        'user': 'toniagonzalez',
        'password': '',
    }
]