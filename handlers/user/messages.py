from aiogram import Router, Bot
from aiogram.types import Message
from database import is_user_registered, bot_message_ids
from services.user.mentions import handle_mentions

router = Router()

# Обработчик сообщений
@router.message()
async def handle_messages(message: Message, bot: Bot):
    user = message.from_user
    if user.is_bot or message.chat.type == 'private':
        return  # Игнорируем сообщения от ботов и в личных чатах
    # Проверяем, есть ли юзер в базе данных
    if not is_user_registered(user.id):
        await message.delete()
        bot_message = await message.answer("Используйте /start, чтобы начать писать сообщения")
        bot_message_ids[message.from_user.id] = bot_message.message_id
        return  # Прекращаем дальнейшую обработку, если юзер не авторизован
    await handle_mentions(message, bot)  # Обрабатываем упоминания
