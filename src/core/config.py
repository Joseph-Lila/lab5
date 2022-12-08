""" Module core.config """
import os
import pathlib

from dotenv import load_dotenv

dotenv_path = pathlib.Path(__file__).parent.parent.parent / '.env'

if dotenv_path.exists():
    load_dotenv(dotenv_path)


def get_redis_host_and_port():
    host = os.environ.get("REDIS_HOST", "localhost")
    port = 63791 if host == "localhost" else 6379
    return dict(host=host, port=port)


def get_sqlite_uri():
    """ Returns sqlite database uri """
    return os.environ.get('SQLITE_DB', 'sqlite://')


def get_email_host_and_port():
    """ Returns email host and port """
    host = os.environ.get("EMAIL_HOST", "localhost")
    port = 11025 if host == "localhost" else 1025
    http_port = 18025 if host == "localhost" else 8025
    return dict(host=host, port=port, http_port=http_port)
