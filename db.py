import mysql.connector


class Database:
    def __init__(self, username, passwd, db_name, table_name):
        self.localhost = "localhost"
        self.username = username
        self.password = passwd
        self.database_name = db_name
        self.table_name = table_name
        try:
            self.create_connection()
        except mysql.connector.errors.ProgrammingError:
            self.create_db()
            self.create_connection()

    def create(self, name, price, link, note):
        cursor = self.db.cursor()

        cursor.execute(
            "INSERT INTO " + self.table_name + " (name, price, link, note) VALUES (%s, %s, %s, %s)",
            (name, price, link, note)
        )

        self.db.commit()

    def read(self):
        cursor = self.db.cursor()

        cursor.execute("SELECT * FROM " + self.table_name + "")

        result = cursor.fetchall()

        return result

    def update(self, id, name, price, link, note):
        cursor = self.db.cursor()

        cursor.execute(
            "UPDATE " + self.table_name + " SET name=%s, price=%s, link=%s, note=%s WHERE id=%s",
            (name, price, link, note, id)
        )

        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()

        cursor.execute("DELETE FROM " + self.table_name + " WHERE id = %s", (id,))

        self.db.commit()

    def create_connection(self):
        db = mysql.connector.connect(
            host=self.localhost,
            user=self.username,
            passwd=self.password,
            database=self.database_name
        )

        self.db = db

    def create_db(self):
        db = mysql.connector.connect(
            host=self.localhost,
            user=self.username,
            passwd=self.password,
        )

        self.db = db

        cursor = self.db.cursor()

        cursor.execute("DROP DATABASE IF EXISTS wishlist")
        cursor.execute("CREATE DATABASE wishlist")

        cursor.execute("USE wishlist")
        cursor.execute('''
            CREATE TABLE wishes(
            id INT PRIMARY KEY AUTO_INCREMENT,
            name CHAR(50) NOT NULL UNIQUE,
            price INT,
            link CHAR(255),
            note CHAR(255)
        )''')

        self.db.commit()