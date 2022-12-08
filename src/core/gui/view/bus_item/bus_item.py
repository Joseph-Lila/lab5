from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivymd.uix.card import MDCard


class BusItem(MDCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.item_id = 0


Factory.register(classname="BusItem", cls=BusItem)
