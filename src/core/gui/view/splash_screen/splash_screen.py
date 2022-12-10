from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

from src.core.gui.view.subscriber import Subscriber


class SplashScreenView(MDScreen, Subscriber):
    """ A class that implements the visual representation `SplashScreenModel` """

    presenter = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def model_is_changed(self, **kwargs):
        """ The method is called when the model changes. """
