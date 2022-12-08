""" Module core.domain.bus """
from dataclasses import dataclass, field


@dataclass
class Bus:
    """ Dataclass representing a bus. """
    item_id: int = field(init=False)
    fio: str
    bus_number: str
    route_number: int
    brand: str
    creation_year: int
    vehicle: float


@dataclass
class Train:
    """ Dataclass representing a train """
    item_id: int = field(init=False)
    title: str
    departure: str
    destination: str
