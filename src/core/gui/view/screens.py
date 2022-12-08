from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.screen import MDScreen

from src.core.gui.model.main_container import MainContainerModel
from src.core.gui.model.map_screen import MapScreenModel
from src.core.gui.model.splash_screen import SplashScreenModel
from src.core.gui.model.bus_screen import BusScreenModel
from src.core.gui.model.train_screen import TrainScreenModel
from src.core.gui.presenter.main_container import MainContainerPresenter
from src.core.gui.presenter.map_screen import MapScreenPresenter
from src.core.gui.presenter.splash_screen import SplashScreenPresenter
from src.core.gui.presenter.bus_screen import BusScreenPresenter
from src.core.gui.presenter.train_screen import TrainScreenPresenter
from src.core.gui.view.home_screen.home_screen import HomeScreenView
from src.core.service_layer.unit_of_work.sqlalchemy_unit_of_work import SqlAlchemyUnitOfWork

SCREENS = {
    # name screen
    "main container": {
        "model": MainContainerModel,
        "presenter": MainContainerPresenter
    },
    "map screen": {
        "model": MapScreenModel,
        "presenter": MapScreenPresenter
    },
    "splash screen": {
        "model": SplashScreenModel,
        "presenter": SplashScreenPresenter
    },
    "bus screen": {
        "model": BusScreenModel,
        "presenter": BusScreenPresenter
    },
    "train screen": {
        "model": TrainScreenModel,
        "presenter": TrainScreenPresenter
    }
}


class ScreensGenerator:
    """
    Creating and adding screens to the screen manager.
    You should not change this cycle unnecessarily. He is self-sufficient.
    """

    def __init__(self, screens=SCREENS):
        self.screens = screens
        self.uow = SqlAlchemyUnitOfWork()

    def generate_splash_screen(self):
        return self._generate_view('splash screen')

    def generate_resulted_view(self):
        screen = MDScreen(name='main container')
        anchor_layout = AnchorLayout()
        main_container_view = self._generate_view('main container')
        main_container_view.screen_master = self._fill_screen_master(
            main_container_view.screen_master,
            [
                'map screen',
                'bus screen',
                'train screen',
            ]
        )
        main_container_view.add_widget(main_container_view.screen_master)
        main_container_view.screen_master.add_widget(HomeScreenView(name='home screen'))
        anchor_layout.add_widget(main_container_view)
        screen.add_widget(anchor_layout)
        return screen

    def _generate_view(self, key):
        model = self.screens[key]['model']()
        presenter = self.screens[key]['presenter'](model, self.uow)
        view = presenter.get_screen()
        view.name = key
        return view

    def _fill_screen_master(self, screen_master, screens_keys: list):
        for screen_key in screens_keys:
            screen_master.add_widget(self._generate_view(screen_key))
        return screen_master
