from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivymd.uix.screen import MDScreen
from src.core.gui.view.subscriber import Subscriber
from src.core.gui.view.bus_item import bus_item
from src.core.domain.model import Bus


class BusScreenView(MDScreen, Subscriber):
    """ A class that implements the visual representation `MapScreenModel` """

    presenter = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def model_is_changed(self, **kwargs):
        """ The method is called when the model changes. """
        new_one: Bus = kwargs.get('new_one', None)
        list_contains_substring = kwargs.get('list_contains_substring', None)
        if new_one:
            self.append_widget(new_one)
        elif list_contains_substring:
            self.buses.clear_widgets()
            for item in list_contains_substring:
                self.append_widget(item)

    def append_widget(self, bus: Bus):
        new_widget = bus_item.BusItem()
        new_widget.item_id = bus.item_id
        new_widget.fio.text = str(bus.fio)
        new_widget.bus_number.text = str(bus.bus_number)
        new_widget.route_number.text = str(bus.route_number)
        new_widget.brand.text = str(bus.brand)
        new_widget.creation_year.text = str(bus.creation_year)
        new_widget.vehicle.text = str(bus.vehicle)
        self.buses.add_widget(new_widget)