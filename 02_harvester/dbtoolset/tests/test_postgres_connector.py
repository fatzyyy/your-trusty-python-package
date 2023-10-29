import pytest
from dbtoolset.postgres_connector import PostgresConnector


@pytest.fixture
def postgres_connector():
    return PostgresConnector(
        host="localhost",
        user="test_user",
        password="test_password",
        database="test_db",
    )


def test_postgres_query(postgres_connector):
    results = postgres_connector.query("SELECT * FROM test_table")
    assert len(results) > 0


def test_postgres_close(postgres_connector):
    postgres_connector.close()
    with pytest.raises(Exception):
        postgres_connector.query("SELECT * FROM test_table")
