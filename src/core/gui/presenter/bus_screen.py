import copy
import time

from src.core.domain.model import Bus
from src.core.gui.view.bus_item.bus_item import BusItem
from src.core.gui.view.bus_screen.bus_screen import BusScreenView
from src.core.service_layer.unit_of_work.abstract_unit_of_work import \
    AbstractUnitOfWork


class BusScreenPresenter:
    """
    The `BusScreenPresenter` class represents a presenter implementation.
    Coordinates work of the view with the model.

    The presenter implements the strategy pattern. The presenter connects to
    the view to control its actions.
    """

    def __init__(self, model, uow):
        """
        The constructor takes a reference to the model.
        The constructor creates the view.
        """
        self.model = model
        self.uow: AbstractUnitOfWork = uow
        self.view = BusScreenView(presenter=self, model=self.model)
        self.list()

    def get_screen(self):
        """ The method creates get the view. """

        return self.view

    def on_text_search(self, instance, value):
        self.model.send_list_contains_substring(value)

    def list(self):
        with self.uow:
            collection = self.uow.buses.list()
            self.model.list(collection)

    def on_edit(self, item_id, fio, bus_number, route_number, brand, creation_year, vehicle):
        bus = Bus(fio, bus_number, route_number, brand, creation_year, vehicle)
        bus.item_id = item_id
        with self.uow:
            self.uow.buses.update(bus)
            self.uow.commit()
        self.model.edit(copy.copy(bus))

    def on_delete(self, item_id: int):
        with self.uow:
            self.uow.buses.delete(item_id)
            self.uow.commit()
        self.model.delete(item_id)

    def create_bus(self, popup_cls, *args):
        popup_cls = popup_cls[0]
        bus = Bus(
            popup_cls.fio.text,
            popup_cls.bus_number.text,
            int(popup_cls.route_number.text),
            popup_cls.brand.text,
            int(popup_cls.creation_year.text),
            float(popup_cls.vehicle.text)
        )

        with self.uow:
            self.uow.buses.add(bus)
            self.uow.commit()
        self.model.add_bus(bus)

    def route_number(self, popup_cls, *args):
        popup_cls = popup_cls[0]
        self.model.send_list_with_route_number(int(popup_cls.route_number.text))

    def show_old(self, *args):
        self.model.show_old()

    def show_with_big_vehicle(self, *args):
        self.model.show_with_big_vehicle()