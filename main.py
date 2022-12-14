from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import platform
from kivymd.app import MDApp

from src.core.adapters.orm import start_mappers
from src.core.gui.view.screens import ScreensGenerator

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions(
        [
            Permission.INTERNET,
            Permission.VIBRATE,
            Permission.READ_EXTERNAL_STORAGE,
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.ACCESS_FINE_LOCATION,
            Permission.ACCESS_COARSE_LOCATION,
        ]
    )


start_mappers()


class MyMVPApp(MDApp):
    title = "LLK Bus Station"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.material_style = "M3"
        self.sm = ScreenManager()
        self.sm.add_widget(ScreensGenerator().generate_splash_screen())
        return self.sm

    def on_start(self):
        Clock.schedule_once(self.login, 18)
        self.sm.add_widget(ScreensGenerator().generate_resulted_view())

    def login(self, *args):
        self.sm.current = 'main container'


if __name__ == '__main__':
    MyMVPApp().run()
