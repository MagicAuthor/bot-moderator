import re
import aiohttp
from aiogram import Bot
from aiogram.types import Message
from config import GROUP_ID, API_TOKEN_ADMIN

import logging

# Обработчик тегов бота
async def handle_mentions(message: Message, bot: Bot):

    # можно напрямую задать username бота строкой в конфиге
    info = await bot.get_me()
    bot_username = info.username

    if bot_username in message.text:
        # Удаление упоминания бота из текста сообщения
        cleaned_message_text = re.sub(r'@\S+', '', message.text).strip()
        print(cleaned_message_text)
        response_text = f"<b>@{message.from_user.username} пишет:</b>\n{cleaned_message_text}\n"
        if message.reply_to_message:
            print(message.reply_to_message.text)
            response_text += (f"<b>В ответ от @{message.reply_to_message.from_user.username}:</b>\n"
                              f"{message.reply_to_message.text}")
        async with aiohttp.ClientSession() as session:
            payload = {
                "chat_id": GROUP_ID,
                "text": response_text,
                "parse_mode": "HTML"
            }
            async with session.post(f"https://api.telegram.org/bot{API_TOKEN_ADMIN}/sendMessage", json=payload) as resp:
                await resp.json()
