""" Module core.service_layer.observer """

from src.core.domain.event.event import Event


class Subscriber:
    """ Abstract superclass for all observers. """

    def model_is_changed(self, event: Event) -> None:
        """
        The method that will be called on the observer when the model changes.
        :return: None
        """
