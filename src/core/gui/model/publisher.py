""" Module core.gui.model """


class Publisher:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, **kwargs):
        for x in self._observers:
            x.model_is_changed(**kwargs)
