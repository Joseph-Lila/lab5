""" Module core.service_layer.observer """


class Subscriber:
    """ Abstract superclass for all observers. """

    def model_is_changed(self, **kwargs) -> None:
        """
        The method that will be called on the observer when the model changes.
        :return: None
        """
