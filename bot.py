from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = '6645562060:AAEr_Lr-Eb0_SQG4KlG6c-GYups4wJiOns8'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Hello!')

@dp.message(Command(commands=['help']))
async def process_help_comand(message: Message):
    await message.answer('заглушка по хэлперу')

@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )

if __name__ == '__main__':
    dp.run_polling(bot)
