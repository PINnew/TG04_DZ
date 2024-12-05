import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN

# Создаем экземпляр бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Определяем инлайн-клавиатуру
inline_keyboards = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Видео", url="https://www.youtube.com/")]
])

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветики, я бот!", reply_markup=inline_keyboards)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())