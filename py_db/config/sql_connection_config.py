# config/sql_connection _config.py

from typing import Optional
from .base_connection_config import BaseConnectionConfig


class SqlConnectionConfig(BaseConnectionConfig):
    """
    Configuration class for holding database connection details.
    """

    def __init__(
        self,
        host: str,
        user: str,
        password: str,
        database: str,
        port: Optional[int] = None,
    ):
        """
        Initialize the configuration with connection details.

        :param host: Database host address.
        :param user: Database user name.
        :param password: Database user password.
        :param database: Database name.
        :param port: Optional port number for the database connection.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
