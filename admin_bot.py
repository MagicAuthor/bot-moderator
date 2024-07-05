import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from config import API_TOKEN_ADMIN
from handlers.admin import register_handlers

async def main() -> None:
    bot = Bot(token=API_TOKEN_ADMIN, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    dp.include_router(register_handlers())

    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
