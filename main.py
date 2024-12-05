import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TOKEN
import keyboard as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветики, я бот!", reply_markup=kb.inline_test)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())