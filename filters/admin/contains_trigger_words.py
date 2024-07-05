from aiogram.filters import BaseFilter
from aiogram.types import Message

class ContainsTriggerWordsFilter(BaseFilter):
    def __init__(self, triggers):
        self.triggers = triggers

    async def __call__(self, message: Message) -> bool:
        if not message.text:  # Проверяем наличие текста
            return False
        return any(trigger in message.text.lower() for trigger in self.triggers)
