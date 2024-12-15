from dotenv import load_dotenv
import os

load_dotenv()


DB_NAME = os.environ.get("database_name")
DB_TEST_NAME = os.environ.get("database_test_name")
DB_USER = os.environ.get("database_user")
DB_PASSWORD = os.environ.get("database_password")
