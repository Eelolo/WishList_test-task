import mysql.connector


class Database:
    def __init__(self, username, passwd, db_name, table_name):
        self.localhost = "localhost"
        self.username = username
        self.password = passwd
        self.database_name = db_name
        self.table_name = table_name
        self.create_connection()

    def create_connection(self):
        db = mysql.connector.connect(
            host=self.localhost,
            user=self.username,
            passwd=self.password,
            database=self.database_name
        )

        self.db = db