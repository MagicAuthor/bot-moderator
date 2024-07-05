from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database import user_message_ids

router = Router()

# Обработчик команды /start
@router.message(CommandStart())
async def start_command(message: Message) -> None:
    user_message_ids[message.from_user.id] = message.message_id
    user_id = message.from_user.id
    await message.answer(
        "Для подтверждения нажмите кнопку ниже",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Нажмите, чтобы писать сообщения", callback_data=f"confirm:{user_id}")]
            ]
        )
    )
