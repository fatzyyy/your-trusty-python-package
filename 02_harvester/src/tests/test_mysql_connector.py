import pytest
from dbtoolset.mysql_connector import MySQLConnector


@pytest.fixture
def mysql_connector():
    return MySQLConnector(
        host="localhost",
        user="test_user",
        password="test_password",
        database="test_db",
    )


def test_mysql_query(mysql_connector):
    results = mysql_connector.query("SELECT * FROM test_table")
    assert len(results) > 0


def test_mysql_close(mysql_connector):
    mysql_connector.close()
    with pytest.raises(Exception):
        mysql_connector.query("SELECT * FROM test_table")
