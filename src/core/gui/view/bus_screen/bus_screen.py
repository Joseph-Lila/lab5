from functools import partial

from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen

from src.core.domain.model import Bus
from src.core.gui.view.bus_item import bus_item
from src.core.gui.view.subscriber import Subscriber


class BusScreenView(MDScreen, Subscriber):
    """ A class that implements the visual representation `MapScreenModel` """

    presenter = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        menu_items = [
            {
                "text": "Create",
                "viewclass": "OneLineListItem",
                "on_release": self.creation_popup
            },
            {
                "text": "Buses with certain `route number`",
                "viewclass": "OneLineListItem",
                "on_release": self.route_number_popup
            },
            {
                "text": "Old buses",
                "viewclass": "OneLineListItem",
                "on_release": self.presenter.show_old
            },
            {
                "text": "Buses with big vehicle",
                "viewclass": "OneLineListItem",
                "on_release": self.presenter.show_with_big_vehicle
            }
        ]
        self.menu = MDDropdownMenu(
            caller=self.cog,
            items=menu_items,
            width_mult=5,
        )
        self.creation_popup_content_cls = None
        self.route_number_popup_content_cls = None

    def model_is_changed(self, **kwargs):
        """ The method is called when the model changes. """
        new_one: Bus = kwargs.get('new_one', None)
        buses_collection = kwargs.get('buses_collection', None)
        delete_one = kwargs.get('delete_one', None)
        if new_one:
            self.append_widget(new_one)
        elif buses_collection:
            self.buses.clear_widgets()
            for item in buses_collection:
                self.append_widget(item)
        elif delete_one is not None:
            ind = [i for i, child in enumerate(self.buses.children) if child.item_id == delete_one][0]
            self.buses.remove_widget(self.buses.children[ind])

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

    def creation_popup(self, *args):
        self.creation_popup_content_cls = Factory.DialogCreateBus()
        buttons = Factory.OKButton(on_press=partial(self.presenter.create_bus, (self.creation_popup_content_cls,)))
        MDDialog(
            title="Create bus",
            type="custom",
            content_cls=self.creation_popup_content_cls,
            buttons=[buttons]
        ).open()

    def route_number_popup(self, *args):
        self.route_number_popup_content_cls = Factory.DialogRouteNumber()
        buttons = Factory.OKButton(on_press=partial(self.presenter.route_number, (self.route_number_popup_content_cls,)))
        MDDialog(
            title="Buses with a certain route number",
            type="custom",
            content_cls=self.route_number_popup_content_cls,
            buttons=[buttons]
        ).open()
