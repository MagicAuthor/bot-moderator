from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
from database import add_user, user_message_ids, bot_message_ids

router = Router()

# Обработчик подтверждения
@router.callback_query(F.data.startswith("confirm:"))
async def confirm_callback_handler(callback_query: CallbackQuery, bot: Bot) -> None:
    user_id = int(callback_query.data.split(":")[1])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("Вы не можете использовать эту кнопку", show_alert=True)
        return
    user = callback_query.from_user
    add_user(user.username, user.id)
    await callback_query.answer("Теперь вы можете писать сообщения")
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    # Удаление сообщения пользователя с вызовом /start
    if user.id in user_message_ids:
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=user_message_ids[user.id])
        del user_message_ids[user.id]
    # Удаление сообщения бота
    if user.id in bot_message_ids:
        await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=bot_message_ids[user.id])
        del bot_message_ids[user.id]
