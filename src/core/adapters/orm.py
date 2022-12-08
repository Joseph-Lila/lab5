""" Module core.adapters.orm """
from sqlalchemy import Column, Float, Integer, MetaData, String, Table
from sqlalchemy.orm import mapper

from src.core.domain.entities.bus import Bus
from src.core.domain.entities.train import Train

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
    mapper(Bus, bus)
    mapper(Train, train)

