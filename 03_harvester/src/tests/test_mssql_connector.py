import pytest
from dbtoolset.mssql_connector import MSSQLConnector


@pytest.fixture
def mssql_connector():
    return MSSQLConnector(
        host="localhost",
        user="test_user",
        password="test_password",
        database="test_db",
    )


def test_mssql_query(mssql_connector):
    results = mssql_connector.query("SELECT * FROM test_table")
    assert len(results) > 0


def test_mssql_close(mssql_connector):
    mssql_connector.close()
    with pytest.raises(Exception):
        mssql_connector.query("SELECT * FROM test_table")
