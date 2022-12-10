from kivy.properties import ObjectProperty
from kivy.utils import platform
from kivy_garden.mapview import MapMarker, MapView
from kivymd.uix.screen import MDScreen
from plyer import gps

from src.core.gui.view.subscriber import Subscriber


class MapScreenView(MDScreen, Subscriber):
    """ A class that implements the visual representation `MapScreenModel` """

    presenter = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def model_is_changed(self, **kwargs):
        """ The method is called when the model changes. """
        lat = kwargs.get('lat', 0)
        lon = kwargs.get('lon', 0)
        self.my_marker.lat = lat
        self.my_marker.lon = lon
