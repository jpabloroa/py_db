# config/sql_connection _config.py

from dotenv import load_dotenv, dotenv_values
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

    env_file_path: str = ".env"

    @classmethod
    def set_env_config_file(cls, file_path: str) -> None:
        """
        Set the path of configuration file

        :param file_path: Path to configuration file, by default is '.env'.
        """
        cls.env_file_path = file_path

    @classmethod
    def load_credential(cls, credential_name: str, throw_on_error: bool = True):
        """
        Load the specified credential into a new class instance

        :param credential_name: Name of the credential, it must match with the prefix (followed by '_') of the defined variables.
        :param throw_on_error: Determines if on an error, the function throws up an exception
        """
        load_dotenv(dotenv_path=cls.env_file_path)

        config_values = dotenv_values()

        class_variables = [
            "host",
            "user",
            "password",
            "database",
            "port",
        ]

        config_variable_names = [
            f"{credential_name.upper()}_{variable}" for variable in class_variables
        ]

        if throw_on_error & (
            len(
                [
                    variable_name
                    for variable_name in config_values.keys()
                    if variable_name.upper() in config_variable_names
                ]
            )
            == 0
        ):
            raise Exception(
                "There no connection keys that satisfy the credential syntax. '{credential name}_{variable name}'"
            )

        return cls(
            **{
                variable: config_values.get(f"{credential_name.upper()}_{variable}")
                for variable in class_variables
            }
        )
