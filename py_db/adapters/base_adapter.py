# adapters/base_adapter.py

from abc import ABC, abstractmethod
from ..config.base_connection_config import BaseConnectionConfig
from typing import Optional, Dict, List


class BaseAdapter(ABC):
    """
    Abstract base class for all database adapters.
    All adapters must implement the methods defined here.
    """

    def __init__(self, config: BaseConnectionConfig):
        """
        Initialize the adapter with the given connection configuration.

        :param config: BaseConnectionConfig object containing connection details.
        """
        self.config = config

    @abstractmethod
    def connect(self):
        """Establish a connection to the database."""
        pass

    @abstractmethod
    def disconnect(self):
        """Close the connection to the database."""
        pass

    @abstractmethod
    def execute_query(self, query: str, params: Optional[Dict] = None):
        """
        Execute a given SQL query.

        :param query: SQL query string to execute.
        :param params: Optional dictionary of query parameters.
        """
        pass

    @abstractmethod
    def fetch_all(self, query: str, params: Optional[Dict] = None) -> List[Dict]:
        """
        Fetch all results from the executed query.

        :param query: SQL query string to execute.
        :param params: Optional dictionary of query parameters.
        :return: List of dictionaries containing the query results.
        """
        pass
