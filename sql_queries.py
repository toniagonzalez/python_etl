#sql queries by database


#locations db queries
locations_db_selection = ('''
    SELECT branch_name FROM "branch_locations" ORDER BY branch_name ASC;
''')

locations_db_insert = ('''
    INSERT INTO library_location_name (branch_locations) VALUES (%s);
''')

#patrons db queries
patrons_db_selection = ('''
    SELECT email_address FROM "patron_list";
''')

patrons_db_insert = ('''
    INSERT INTO patron_email_list (email_address) VALUES (%s);
''')

#librarymanager db queries
librarymanager_db_selection = ('''
    SELECT title FROM "Books" ORDER BY title ASC;
''')

librarymanager_db_insert = ('''
    INSERT INTO book_inventory (books) VALUES (%s);
''')

#exports queries
class SqlQuery:
    def __init__(self, select_query, load_query):
        self.select_query = select_query
        self.load_query = load_query

#SqlQuery instances per database
locations_db_query = SqlQuery(locations_db_selection, locations_db_insert)
patrons_db_query = SqlQuery(patrons_db_selection, patrons_db_insert)
librarymanager_db_query = SqlQuery(librarymanager_db_selection, librarymanager_db_insert)

#store queries as list for iteration
locations_db_queries = [locations_db_query]
patrons_db_queries = [patrons_db_query]
librarymanager_db_queries = [librarymanager_db_query]