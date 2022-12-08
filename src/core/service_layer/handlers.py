from __future__ import annotations
from dataclasses import asdict
from typing import List, Dict, Callable, Type, TYPE_CHECKING
from src.core.domain.event.event import Event
from src.core.domain.command.command import Command

if TYPE_CHECKING:
    from src.core.adapters.notification import *
    from src.core.service_layer.unit_of_work import *


EVENT_HANDLERS = {

}  # type: Dict[Type[Event], List[Callable]]

COMMAND_HANDLERS = {

}  # type: Dict[Type[Command], Callable]
