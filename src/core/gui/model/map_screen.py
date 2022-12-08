from src.core.gui.model.publisher import Publisher
import pathlib
import shutil
import atexit
from plyer import gps
from kivy.utils import platform


def clear_cache_dir():
    path = pathlib.Path('cache')
    if path.exists():
        shutil.rmtree(path)


class MapScreenModel(Publisher):
    """ The MapScreenModel class is a unit of work model implementation. """

    def __init__(self):
        super().__init__()
        self.on_start()
        atexit.register(self.on_exit)

    def on_start(self):
        clear_cache_dir()
        if platform in ['android', 'ios']:
            gps.configure(on_location=self.on_gps_location)
            gps.start(minTime=1000, minDistance=0)

    def on_exit(self):
        if platform in ['android', 'ios']:
            gps.stop()
        clear_cache_dir()

    def on_gps_location(self, **kwargs):
        lat, lon = kwargs.get('lat', 0), kwargs.get('lon', 0)
        self.notify_observers(lat=lat, lon=lon)
