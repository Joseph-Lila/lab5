""" Module core.gui.view.main_container """

from kivy.properties import ObjectProperty
from kivymd.uix.card import MDCard

from src.core.gui.view.subscriber import Subscriber


class MainContainerView(MDCard, Subscriber):
    """ A class that implements the visual presentation `MainContainerModel` """

    presenter = ObjectProperty()
    model = ObjectProperty()
    screen_master = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)  # register the view as an observer

    def model_is_changed(self, **kwargs):
        """ The method is called when the model changes. """
