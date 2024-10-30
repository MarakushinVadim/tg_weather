from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from main import get_weather

BOT_TOKEN = '6645562060:AAEr_Lr-Eb0_SQG4KlG6c-GYups4wJiOns8'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Hello!')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Чтобы получть прогоноз погоды отправь мне название города')


@dp.message()
async def send_weather(message: Message):
    if message.text:
        weather = get_weather(message.text)
        await message.reply(weather)
    else:
        await message.reply(
            text='Введите название города для получения погоды'
        )

if __name__ == '__main__':
    dp.run_polling(bot)
