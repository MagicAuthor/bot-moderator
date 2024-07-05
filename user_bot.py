import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from config import API_TOKEN_USER
from handlers.user import register_handlers

async def main() -> None:
    # Инициализация бота и диспетчера
    bot = Bot(token=API_TOKEN_USER, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()
    dp.include_router(register_handlers())

    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
