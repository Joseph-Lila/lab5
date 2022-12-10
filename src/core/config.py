""" Module core.config """
import pathlib

from dotenv import load_dotenv

app_path = pathlib.Path(__file__).parent.parent.parent
dotenv_path = app_path / '.env'
database_path = app_path / 'assets' / 'databases' / 'sqlite.db'

if dotenv_path.exists():
    load_dotenv(dotenv_path)


def get_sqlite_uri():
    """ Returns sqlite database uri """
    return f"sqlite:///{database_path}"
