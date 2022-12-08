""" Module core.adapters.repository.bus_repository """
from typing import List, Optional

from src.core.adapters.repository.abstract_repository import AbstractRepository
from src.core.domain.model import Train


class TrainRepository(AbstractRepository):
    """ Repository for train items. """
    def __init__(self, session):
        self.session = session

    def add(self, item: Train) -> None:
        self.session.add(item)

    def get_by_id(self, item_id: int) -> Optional[Train]:
        return self.session.query(Train).filter_by(item_id == item_id).one()

    def list(self) -> List[Train]:
        return self.session.query(Train).all()

    def update(self, item: Train) -> None:
        self.session.query(Train).filter_by(item_id=item.item_id).update(
            title=item.title, departure=item.departure, destination=item.destination)

    def delete(self, item: Train) -> None:
        self.session.query(Train).filter_by(item_id=item.item_id).delete()
