from src.core.gui.view.bus_screen.bus_screen import BusScreenView
from src.core.service_layer.unit_of_work.abstract_unit_of_work import AbstractUnitOfWork
from src.core.gui.view.bus_item.bus_item import BusItem


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

    def get_screen(self):
        """ The method creates get the view. """

        return self.view

    def on_text_search(self, instance, value):
        print(value)

