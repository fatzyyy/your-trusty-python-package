import psycopg2


class PostgresConnector:
    def __init__(self, host, user, password, database):
        self.connection = psycopg2.connect(
            host=host, user=user, password=password, database=database
        )
        self.cursor = self.connection.cursor()

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
