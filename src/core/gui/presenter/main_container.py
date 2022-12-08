from kivy.uix.screenmanager import ScreenManager

from src.core.gui.view.main_container.main_container import MainContainerView


class MainContainerPresenter:
    """
    The `MainContainerPresenter` class represents a presenter implementation.
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
        self.view = MainContainerView(
            presenter=self,
            model=self.model,
            screen_master=ScreenManager()
        )

    def get_screen(self):
        """ The method creates get the view. """

        return self.view

    def on_press_nav_item(self, screen_name):
        self.view.screen_master.current = screen_name

    def on_press_home_btn_item(self):
        self.view.screen_master.current = 'home screen'
