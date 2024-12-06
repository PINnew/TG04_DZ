import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from config import TOKEN
import keyboard as kb

# Создаем экземпляр бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветики, я бот!", reply_markup=kb.inline_test)

@dp.message(Command(commands=["dynamic"]))
async def dynamic(message: Message):
    await message.answer("Нажмите покажу больше опций.", reply_markup=kb.start_keyboard)

@dp.callback_query()
async def handle_callback(callback_query: CallbackQuery):
    if callback_query.data == "show_more":
        # Заменяем кнопку "Показать больше" на новые кнопки
        await callback_query.message.edit_reply_markup(reply_markup=kb.dynamic_keyboard)
    elif callback_query.data == "option_1":
        await callback_query.message.answer("Вы выбрали Опция 1!")
    elif callback_query.data == "option_2":
        await callback_query.message.answer("Вы выбрали Опция 2!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
