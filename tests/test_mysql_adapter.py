# test_mysql_adapter.py

import unittest
from ..py_db.adapters.mysql_adapter import MySQLAdapter
from ..py_db.config.sql_connection_config import SqlConnectionConfig
from ..py_db.database_manager import DatabaseManager


class TestMySQLAdapter(unittest.TestCase):
    def setUp(self):
        """Set up the test with connection configuration for MySQL."""
        self.config = SqlConnectionConfig(
            host="localhost",
            user="your_mysql_username",
            password="your_mysql_password",
            database="your_database_name",
        )
        self.adapter = MySQLAdapter(self.config)
        self.db_manager = DatabaseManager(self.adapter)

    def test_mysql_connection(self):
        """Test MySQL connection by executing 'SELECT 1'."""
        try:
            self.db_manager.connect()
            result = self.db_manager.fetch_all("SELECT 1")
            self.assertEqual(result, [{"1": 1}])
        finally:
            self.db_manager.disconnect()


if __name__ == "__main__":
    unittest.main()
