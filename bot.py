import logging
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5026970138:AAGjboqxlPG1jnX3GMMXzV4bNm0e9N1DnPs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Samandar qalay endi.?")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)