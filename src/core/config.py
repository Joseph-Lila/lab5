""" Module core.config """
import os
import pathlib

from dotenv import load_dotenv

dotenv_path = pathlib.Path(__file__).parent.parent.parent / '.env'

if dotenv_path.exists():
    load_dotenv(dotenv_path)


def get_sqlite_uri():
    """ Returns sqlite database uri """
    return os.environ.get('SQLITE_DB', 'sqlite://')
