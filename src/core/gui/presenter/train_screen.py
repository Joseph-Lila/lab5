from src.core.gui.view.train_screen.train_screen import TrainScreenView


class TrainScreenPresenter:
    """
    The `TrainScreenPresenter` class represents a presenter implementation.
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
        self.uow = uow
        self.view = TrainScreenView(presenter=self, model=self.model)
        self.data = []

    def get_screen(self):
        """ The method creates get the view. """

        return self.view
