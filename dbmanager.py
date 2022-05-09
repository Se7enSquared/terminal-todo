import sqlite3

class DatabaseManager:
    ''' Terminal-ToDo Database Manager '''

    def __init__(self, db_name):
            self.db_name = db_name
            self.conn = None
            print(f'Databse {db_name} created successfully')
    
    @classmethod
    def check_database(cls, db_name):
        ''' Check if the given database exists'''
        try:
            print(f'Checking if {db_name} exists or not...')
            conn = sqlite3.connect(db_name, uri=True)
            print(f'Database exists. Succesfully connected to {db_name}')
            
        except sqlite3.OperationalError as err:
            print('Database does not exist')
            print(err)
    
    def close_connection(self):
        ''' Close database connection'''

        if self.conn is not None:
            self.conn.close()