""" Module core.adapters.orm """
from sqlalchemy import Column, Float, Integer, MetaData, String, Table
from sqlalchemy.orm import mapper
from sqlalchemy import create_engine
from src.core.domain import model
from src.core import config
from sqlalchemy_utils import database_exists
from src.core.domain.fake_constructor import get_fake_bus

metadata = MetaData()

bus = Table(
    "Bus",
    metadata,
    Column("item_id", Integer, primary_key=True, autoincrement=True),
    Column("fio", String(75), nullable=False),
    Column("bus_number", String(10), nullable=False),
    Column("route_number", Integer, nullable=False),
    Column("brand", String(75), nullable=False),
    Column("creation_year", Integer, nullable=False),
    Column("vehicle", Float, nullable=False),
)

train = Table(
    "Train",
    metadata,
    Column("item_id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(75), nullable=False),
    Column("departure", String(75), nullable=False),
    Column("destination", String(75), nullable=False),
)


def start_mappers():
    """ Method to map entities with tables. """
    mapper(model.Bus, bus)
    mapper(model.Train, train)


def create_db(uow):
    """ Method to create database """
    db_uri = config.get_sqlite_uri()
    if not database_exists(db_uri):
        engine = create_engine(db_uri, pool_pre_ping=True)
        with engine.connect() as conn:
            metadata.create_all(conn)
        with uow:
            for i in range(10):
                uow.buses.add(get_fake_bus())
            uow.commit()