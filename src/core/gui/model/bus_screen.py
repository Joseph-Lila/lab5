from src.core.domain.entities.bus import Bus
from src.core.gui.model.publisher import Publisher
from src.core.gui.view.bus_item.bus_item import BusItem


class BusScreenModel(Publisher):
    """ The BusScreenModel class. """

    def __init__(self):
        super().__init__()
        self.data = []
        self.widgets = []

    def add_bus(self, bus: Bus):
        self.data.append(Bus)
        self.widgets.append(
            BusItem(
                item_id=Bus.item_id,
                fio=Bus.fio,
                bus_number=Bus.bus_number,
                route_number=Bus.route_number,
                brand=Bus.brand,
                creation_year=Bus.creation_year,
                vehicle=Bus.vehicle
            )
        )
        self.notify_observers()
