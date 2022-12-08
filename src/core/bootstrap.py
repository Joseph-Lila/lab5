import inspect
from typing import Callable
from src.core.adapters import orm, redis_eventpublisher
from src.core.adapters.notification.abstract_notification import AbstractNotification
from src.core.adapters.notification.email_notification import EmailNotification
from src.core.service_layer.unit_of_work.sqlalchemy_unit_of_work import SqlAlchemyUnitOfWork
from src.core.service_layer.unit_of_work.abstract_unit_of_work import AbstractUnitOfWork
from src.core.service_layer import messagebus, handlers


def bootstrap(
        start_orm: bool = True,
        uow: AbstractUnitOfWork = SqlAlchemyUnitOfWork(),
        notification: AbstractNotification = None,
        publish: Callable = redis_eventpublisher.publish,
) -> messagebus.MessageBus:
    if notification is None:
        notification = EmailNotification()

    if start_orm:
        orm.start_mappers()

    dependencies = {"uow": uow, "notification": notification, "publish": publish}
    injected_event_handlers = {
        event_type: [
            inject_dependencies(handler, dependencies)
            for handler in event_handlers
        ]
        for event_type, event_handlers in handlers.EVENT_HANDLERS.items()
    }
    injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies)
        for command_type, handler in handlers.COMMAND_HANDLERS.items()
    }

    return messagebus.MessageBus(
        uow=uow,
        event_handlers=injected_event_handlers,
        command_handlers=injected_command_handlers,
    )


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency
        for name, dependency in dependencies.items()
        if name in params
    }
    return lambda message: handler(message, **deps)
