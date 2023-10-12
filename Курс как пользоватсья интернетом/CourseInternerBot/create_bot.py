from config import TOKEN
from aiogram import Bot
from aiogram.dispatcher import Dispatcher 

#bot initialization
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)