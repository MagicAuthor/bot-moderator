from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import WHITE_LIST_PHONE_NUMBERS
from database import authorized_admins

router = Router()

# Обработчик команды /login и авторизации по номеру телефона
@router.message(Command("login"))
async def start(message: Message) -> None:
    if message.chat.type != 'private':
        await message.answer("Пожалуйста, отправьте команду /login в личный чат с ботом для авторизации.")
    else:
        await message.answer("Пожалуйста, отправьте свой номер телефона для авторизации.",
                             reply_markup=ReplyKeyboardMarkup(keyboard=[
                                 [KeyboardButton(text="Поделиться контактом", request_contact=True)]
                             ], resize_keyboard=True))

# Обработчик контакта для авторизации
@router.message(F.contact)
async def contact(message: Message) -> None:
    if message.chat.type != 'private':
        await message.answer("Авторизация доступна только в личном чате с ботом.")
    elif message.contact.phone_number in WHITE_LIST_PHONE_NUMBERS:
        authorized_admins.add(message.from_user.id)
        await message.answer("Вы успешно авторизованы!", reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("Вы не являетесь администратором.", reply_markup=ReplyKeyboardRemove())
