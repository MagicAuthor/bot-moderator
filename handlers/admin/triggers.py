from aiogram import Router, Bot
from aiogram.types import Message
from filters.admin.contains_trigger_words import ContainsTriggerWordsFilter
from config import GROUP_ID

router = Router()
# Список запрещенных слов
triggers = ["клоун", "дурак"]  # можно подгрузить из другого файла базу запрещенных слов

# Обработчик триггеров и предупреждения
@router.message(ContainsTriggerWordsFilter(triggers))
async def handle_admin_messages(message: Message, bot: Bot) -> None:
    await bot.delete_message(chat_id=GROUP_ID, message_id=message.message_id)
    await message.answer(f"@{message.from_user.username} не ругайтесь, иначе вас заблокируют")
