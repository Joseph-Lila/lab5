from __future__ import annotations
from typing import List, Dict, Callable, Type, TYPE_CHECKING
from src.core.domain.events import Event
from src.core.domain.commands import Command

if TYPE_CHECKING:
    pass


EVENT_HANDLERS = {

}  # type: Dict[Type[Event], List[Callable]]

COMMAND_HANDLERS = {

}  # type: Dict[Type[Command], Callable]
