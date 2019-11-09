#sql queries by database

#first db
first_db_selection = ('''
    SELECT blah, blah, blah FROM table;
''')

first_db_insert = ('''
    INSERT INTO table (blah, blah, blah) VALUES (???)
''')

#second db
second_db_selection = ('''
    SELECT blah, blah, blah FROM table WHERE blah;
''')

second_db_insert = ('''
    INSERT INTO table (blah, blah, blah) VALUES (???)
''')

#third db
third_db_selection = ('''
    SELECT blah, blah, blah FROM table;
''')

third_db_insert = ('''
    INSERT INTO table (blah, blah, blah) VALUES (???)
''')

#exports queries
class SqlQuery:
    def __init__(self, select_query, load_query):
        self.select_query = select_query
        self.load_query = load_query

#SqlQuery instances per database
first_db_query = SqlQuery(first_db_selection, first_db_insert)
second_db_query = SqlQuery(second_db_selection, second_db_insert)
third_db_query = SqlQuery(third_db_selection, third_db_insert)

#store queries as list for iteration
first_db_queries = [first_db_query]
second_db_queries = [second_db_query]
third_db_queries = [third_db_query]