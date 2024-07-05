import aiohttp
from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from config import GROUP_ID, API_TOKEN_USER
from database import get_user_id_by_username, authorized_admins

router = Router()

# Обработчик команды /ban_user
@router.message(Command("ban"))
async def ban_user(message: Message, bot: Bot) -> None:
    if message.from_user.id not in authorized_admins:
        await message.answer("Для выполнения этой команды авторизуйтесь через команду /login.")
        return
    args = message.text.split()
    if len(args) < 3:
        await message.answer("Использование: /ban @username причина")
        return
    username = args[1]
    reason = " ".join(args[2:])
    try:
        if username.startswith('@'):
            user_id = get_user_id_by_username(username.lstrip('@'))
        else:
            user_id = username
            username = ""
        # Баним пользователя по user_id
        await bot.ban_chat_member(chat_id=GROUP_ID, user_id=user_id)
        async with aiohttp.ClientSession() as session:
            payload = {
                "chat_id": GROUP_ID,
                "text": f"Юзер {username} заблокирован. Причина: {reason}"
            }
            async with session.post(f"https://api.telegram.org/bot{API_TOKEN_USER}/sendMessage", json=payload) as resp:
                await resp.json()
    except Exception as e:
        await message.answer(f"Не удалось заблокировать пользователя {username}. Ошибка: {e}")
