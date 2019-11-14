from variables import *

#(target db, datawarehouse)
datawarehouse_db_config = {
    'dbname': '{}'.format(datawarehouse_name),
    'host': '{}'.format(warehouse_host),
    'port': '{}'.format(warehouse_port),
    'user': '{}'.format(warehouse_user),
    'password': '{}'.format(warehouse_password),
}

#(source db) 'postgres'
source1_db_config = [
    {
        'dbname': '{}'.format(source1_name),
        'host': '{}'.format(source1_host),
        'port': '{}'.format(source1_port),
        'user': '{}'.format(source1_user),
        'password': '{}'.format(source1_password),
    }
]

#(source db) 'postgres'
source2_db_config = [
    {
        'dbname': '{}'.format(source2_name),
        'host': '{}'.format(source2_host),
        'port': '{}'.format(source2_port),
        'user': '{}'.format(source2_user),
        'password': '{}'.format(source2_password),
    }
]

#(source db) 'postgres'
source3_db_config = [
    {
        'dbname': '{}'.format(source3_name),
        'host': '{}'.format(source3_host),
        'port': '{}'.format(source3_port),
        'user': '{}'.format(source3_user),
        'password': '{}'.format(source3_password),
    }
]