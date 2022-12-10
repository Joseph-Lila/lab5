""" Module core.adapters.repository.bus_repository """
from typing import List, Optional

from src.core.adapters.repository.abstract_repository import AbstractRepository
from src.core.domain.model import Bus


class BusRepository(AbstractRepository):
    """ Repository for bus items. """

    def __init__(self, session):
        self.session = session

    def add(self, item: Bus) -> None:
        self.session.add(item)

    def get_by_id(self, item_id: int) -> Optional[Bus]:
        return self.session.query(Bus).filter(item_id == item_id).one()

    def list(self) -> List[Bus]:
        return self.session.query(Bus).all()

    def update(self, item: Bus) -> None:
        self.session.query(Bus).filter_by(item_id=item.item_id).update(
            {"fio": item.fio, 'bus_number': item.bus_number, 'route_number': item.route_number,
             'brand': item.brand, 'creation_year': item.creation_year, "vehicle": item.vehicle})

    def delete(self, _id: int) -> None:
        self.session.query(Bus).filter_by(item_id=_id).delete()
