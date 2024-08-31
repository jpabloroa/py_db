# adapters/postgresql_adapter.py

import psycopg2
from psycopg2 import extensions, sql
from .base_adapter import BaseAdapter
from ..config.sql_connection_config import SqlConnectionConfig
from typing import Optional, Dict, List


class PostgreSQLAdapter(BaseAdapter):
    """
    PostgreSQL database adapter that implements the BaseAdapter interface.
    """

    def __init__(self, config: SqlConnectionConfig):
        super().__init__(config)
        self.connection: Optional[extensions.connection] = None

    def connect(self):
        """Establish a connection to the PostgreSQL database."""
        self.connection = psycopg2.connect(
            host=self.config.host,
            user=self.config.user,
            password=self.config.password,
            dbname=self.config.database,
            port=self.config.port or 5432,
        )

    def disconnect(self):
        """Close the connection to the PostgreSQL database."""
        if self.connection:
            self.connection.close()

    def execute_query(self, query: str, params: Optional[Dict] = None):
        """
        Execute a given SQL query on the PostgreSQL database.

        :param query: SQL query string to execute.
        :param params: Optional dictionary of query parameters.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            self.connection.commit()

    def fetch_all(self, query: str, params: Optional[Dict] = None) -> List[Dict]:
        """
        Fetch all results from the executed query on the PostgreSQL database.

        :param query: SQL query string to execute.
        :param params: Optional dictionary of query parameters.
        :return: List of dictionaries containing the query results.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            columns = [desc[0] for desc in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results
