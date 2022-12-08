import copy

from src.core.domain.model import Bus
from src.core.gui.model.publisher import Publisher
from src.core.gui.view.bus_item.bus_item import BusItem


class BusScreenModel(Publisher):
    """ The BusScreenModel class. """

    def __init__(self):
        super().__init__()
        self.data = []

    def add_bus(self, bus: Bus):
        self.data.append(copy.copy(bus))
        self.notify_observers(new_one=self.data[-1])

    def send_list_contains_substring(self, value):
        list_contains_substring = [bus for bus in self.data if value.lower() in bus.fio.lower()]
        self.notify_observers(list_contains_substring=list_contains_substring)

    def list(self, collection: list):
        for item in collection:
            self.add_bus(item)
