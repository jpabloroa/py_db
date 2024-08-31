# adapters/sqlserver_adapter.py

import pyodbc
from .base_adapter import BaseAdapter
from ..config.sql_connection_config import SqlConnectionConfig
from typing import Optional, Dict, List


class SQLServerAdapter(BaseAdapter):
    """
    SQL Server database adapter that implements the BaseAdapter interface.
    """

    def __init__(self, config: SqlConnectionConfig):
        super().__init__(config)
        self.connection: Optional[pyodbc.Connection] = None

    def connect(self):
        """Establish a connection to the SQL Server database."""
        connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={self.config.host};"
            f"DATABASE={self.config.database};"
            f"UID={self.config.user};"
            f"PWD={self.config.password};"
            f"PORT={self.config.port or 1433};"
        )
        self.connection = pyodbc.connect(connection_string)

    def disconnect(self):
        """Close the connection to the SQL Server database."""
        if self.connection:
            self.connection.close()

    def execute_query(self, query: str, params: Optional[Dict] = None):
        """
        Execute a given SQL query on the SQL Server database.

        :param query: SQL query string to execute.
        :param params: Optional dictionary of query parameters.
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params or {})
        self.connection.commit()
        cursor.close()

    def fetch_all(self, query: str, params: Optional[Dict] = None) -> List[Dict]:
        """
        Fetch all results from the executed query on the SQL Server database.

        :param query: SQL query string to execute.
        :param params: Optional dictionary of query parameters.
        :return: List of dictionaries containing the query results.
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params or {})
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        return results
