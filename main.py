import asyncio
from aiogram import Dispatcher, executor, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN

TOKEN_BOT = TOKEN

loop = asyncio.new_event_loop()
bot = Bot(token=TOKEN_BOT, parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher(bot=bot, loop=loop, storage=storage)


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dispatcher=dp)

