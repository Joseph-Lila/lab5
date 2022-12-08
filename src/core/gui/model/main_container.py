""" Module core.gui.model
    The model implements the observer pattern. This means that the class must
    support adding, removing, and alerting observers. in this case, the model is
    completely independent of controllers and views. It is important that all
    registered observers implement a specific method that will be called by the
    model when they are notified (in this case, it is the `nodel_is_changed`
    method). For this, observers must be descendants of an abstract class,
    inheriting which, the `model_is_changed` method must be overridden.
"""

from src.core.gui.model.publisher import Publisher


class MainContainerModel(Publisher):
    """ The MainContainerModel class is a unit of work model implementation. """
