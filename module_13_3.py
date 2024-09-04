from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import logging
import asyncio
from os import getenv

# Получение токена бота из переменных окружения
API_TOKEN = getenv('TELEGRAM_TOKEN')

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация диспетчера
dp = Dispatcher()

# Обработчик команды /start
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

# Обработчик всех остальных сообщений
@dp.message()
async def echo_handler(message: Message) -> None:
    await message.answer('Введите команду /start, чтобы начать общение.')

async def main() -> None:
    # Инициализация бота с настройками по умолчанию
    bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # Запуск обработки событий
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())