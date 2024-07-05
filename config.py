import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

API_TOKEN_USER = os.getenv('API_TOKEN_USER')
API_TOKEN_ADMIN = os.getenv('API_TOKEN_ADMIN')

# ID группы
GROUP_ID = int(os.getenv('GROUP_ID'))

# Белый список номеров телефонов
WHITE_LIST_PHONE_NUMBERS = os.getenv('WHITE_LIST_PHONE_NUMBERS').split(',')
