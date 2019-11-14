#sql queries by database


#locations db queries
source1_db_selection = ('''
    SELECT branch_name FROM "branch_locations" ORDER BY branch_name ASC;
''')

source1_db_insert = ('''
    INSERT INTO library_location_name (branch_locations) VALUES (%s);
''')

#patrons db queries
source2_db_selection = ('''
    SELECT email_address FROM "patron_list";
''')

source2_db_insert = ('''
    INSERT INTO patron_email_list (email_address) VALUES (%s);
''')

#librarymanager db queries
source3_db_selection = ('''
    SELECT title FROM "Books" ORDER BY title ASC;
''')

source3_db_insert = ('''
    INSERT INTO book_inventory (books) VALUES (%s);
''')

#exports queries
class SqlQuery:
    def __init__(self, select_query, load_query):
        self.select_query = select_query
        self.load_query = load_query

#SqlQuery instances per database
source1_db_query = SqlQuery(source1_db_selection, source1_db_insert)
source2_db_query = SqlQuery(source2_db_selection, source2_db_insert)
source3_db_query = SqlQuery(source3_db_selection, source3_db_insert)

#store queries as list for iteration
source1_db_queries = [source1_db_query]
source2_db_queries = [source2_db_query]
source3_db_queries = [source3_db_query]