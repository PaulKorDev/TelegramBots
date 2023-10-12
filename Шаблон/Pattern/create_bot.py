from aiogram import Bot
from aiogram.dispatcher import Dispatcher 
#from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN

#Если есть fsm
#storage = MemoryStorage()

#bot initialization
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)#, storage=storage)
