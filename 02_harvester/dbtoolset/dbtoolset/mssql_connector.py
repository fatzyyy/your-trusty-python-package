import pyodbc


class MSSQLConnector:
    def __init__(self, host, user, password, database):
        self.connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
            + host
            + ";DATABASE="
            + database
            + ";UID="
            + user
            + ";PWD="
            + password
        )
        self.cursor = self.connection.cursor()

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
