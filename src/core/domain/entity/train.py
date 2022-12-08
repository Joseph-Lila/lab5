""" Module core.domain.train """
from dataclasses import dataclass, field


@dataclass
class Train:
    """ Dataclass representing a train """
    item_id: int = field(init=False)
    title: str
    departure: str
    destination: str
