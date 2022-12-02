from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from all_botton import kb

API_TOKEN = '5983251299:AAE0WGwWrkr45T9IJc6OWvdKFCA4YNFi14w'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

 
@dp.message_handler(commands='calc')
async def command(message: types.Message):
   await message.answer('button', reply_markup = kb)

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)



