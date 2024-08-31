# adapters/mysql_adapter.py

import mysql.connector
from mysql.connector import connection
from .base_adapter import BaseAdapter
from ..config.sql_connection_config import SqlConnectionConfig
from typing import Optional, Dict, List


class MySQLAdapter(BaseAdapter):
    """
    MySQL database adapter that implements the BaseAdapter interface.
    """

    def __init__(self, config: SqlConnectionConfig):
        super().__init__(config)
        self.connection: Optional[connection.MySQLConnection] = None

    def connect(self):
        """Establish a connection to the MySQL database."""
        self.connection = mysql.connector.connect(
            host=self.config.host,
            user=self.config.user,
            password=self.config.password,
            database=self.config.database,
            port=self.config.port or 3306,
        )

    def disconnect(self):
        """Close the connection to the MySQL database."""
        if self.connection:
            self.connection.close()

    def execute_query(self, query: str, params: Optional[Dict] = None):
        """
        Execute a given SQL query on the MySQL database.

        :param query: SQL query string to execute.
        :param params: Optional dictionary of query parameters.
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        cursor.close()

    def fetch_all(self, query: str, params: Optional[Dict] = None) -> List[Dict]:
        """
        Fetch all results from the executed query on the MySQL database.

        :param query: SQL query string to execute.
        :param params: Optional dictionary of query parameters.
        :return: List of dictionaries containing the query results.
        """
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()
        return results
