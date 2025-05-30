from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any

class LanguageMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable, event: Message, data: Dict[str, Any]) -> Any:
        event.conf = {}
        return await handler(event, data)
