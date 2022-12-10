import copy

from src.core.domain.model import Bus
from src.core.gui.model.publisher import Publisher


class BusScreenModel(Publisher):
    """ The BusScreenModel class. """

    def __init__(self):
        super().__init__()
        self.data = []

    def add_bus(self, bus: Bus):
        self.data.append(copy.copy(bus))
        self.notify_observers(new_one=self.data[-1])

    def send_list_contains_substring(self, value):
        buses_collection = [bus for bus in self.data if value.lower() in bus.fio.lower()]
        self.notify_observers(buses_collection=buses_collection)

    def send_list_with_route_number(self, value):
        buses_collection = [bus for bus in self.data if bus.route_number == value]
        self.notify_observers(buses_collection=buses_collection)

    def show_old(self, *args):
        buses_collection = [bus for bus in self.data if abs(bus.creation_year - 2022) > 10]
        self.notify_observers(buses_collection=buses_collection)

    def show_with_big_vehicle(self, *args):
        buses_collection = [bus for bus in self.data if bus.vehicle > 400]
        self.notify_observers(buses_collection=buses_collection)

    def list(self, collection: list):
        for item in collection:
            self.add_bus(item)

    def edit(self, item: Bus):
        ind = [i for i, el in enumerate(self.data) if el.item_id == item.item_id][-1]
        self.data[ind] = item

    def delete(self, item_id: int):
        ind = [i for i, el in enumerate(self.data) if el.item_id == item_id][-1]
        self.data.pop(ind)
        self.notify_observers(delete_one=item_id)
