# database_manager.py

from .adapters.base_adapter import BaseAdapter
from .adapters.mysql_adapter import MySQLAdapter
from .adapters.postgresql_adapter import PostgreSQLAdapter
from .adapters.sqlserver_adapter import SQLServerAdapter
from .config.base_connection_config import BaseConnectionConfig
from typing import Optional, Dict, Union


class DatabaseManager:
    """
    Manager class for handling database connections using different adapters.
    """

    # Map short names to adapter classes
    _adapter_map = {
        "mysql": MySQLAdapter,
        "postgresql": PostgreSQLAdapter,
        "sqlserver": SQLServerAdapter,
        # Add other default adapters here
    }

    def __init__(self, adapter: BaseAdapter):
        """
        Initialize the DatabaseManager with the provided adapter.

        :param adapter: An instance of a class that inherits from BaseAdapter.
        """
        self.adapter = adapter

    def connect(self):
        """Establish a connection using the adapter."""
        self.adapter.connect()

    def disconnect(self):
        """Disconnect the current connection using the adapter."""
        self.adapter.disconnect()

    def execute(self, query: str, params: Optional[Dict] = None):
        """
        Execute a query on the database.

        :param query: SQL query string to execute.
        :param params: Optional dictionary of query parameters.
        """
        self.adapter.execute_query(query, params)

    def fetch_all(self, query: str, params: Optional[Dict] = None):
        """
        Fetch all results for a given query.

        :param query: SQL query string to execute.
        :param params: Optional dictionary of query parameters.
        :return: List of dictionaries containing the query results.
        """
        return self.adapter.fetch_all(query, params)

    @classmethod
    def create(cls, db_type: Union[str, type], config: Dict) -> "DatabaseManager":
        """
        Create a DatabaseManager instance using a specified adapter.

        :param db_type: Either a string key for a predefined adapter or a class that inherits from BaseAdapter.
        :param config: Dictionary of connection configuration options.
        :return: A DatabaseManager instance configured with the specified adapter.
        """
        # Check if db_type is a string, and map it to the appropriate adapter class
        if isinstance(db_type, str):
            adapter_class = cls._adapter_map.get(db_type)
            if not adapter_class:
                raise ValueError(f"No adapter found for db_type '{db_type}'")
        elif issubclass(db_type, BaseAdapter):
            adapter_class = db_type
        else:
            raise ValueError(
                "db_type must be either a string or a subclass of BaseAdapter"
            )

        # Instantiate the adapter with the given config
        config_obj = BaseConnectionConfig(**config)
        adapter = adapter_class(config_obj)
        return cls(adapter)
