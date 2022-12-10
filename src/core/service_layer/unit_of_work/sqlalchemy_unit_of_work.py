from src.core.adapters.repository.bus_repository import BusRepository
from src.core.adapters.repository.train_repository import TrainRepository
from src.core.service_layer.unit_of_work.abstract_unit_of_work import (
    DEFAULT_SESSION_FACTORY, AbstractUnitOfWork)


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    """ SqlAlchemyUnitOfWork implementation for unit of work pattern """

    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        super().__init__()
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory(expire_on_commit=False)
        self.buses = BusRepository(self.session)
        self.trains = TrainRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(self, *args)
        self.session.expunge_all()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
