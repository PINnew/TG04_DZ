import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Инлайн-кнопки
start_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
])

dynamic_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
    [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
])

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Нажмите на кнопку ниже, чтобы продолжить.", reply_markup=start_keyboard)

@dp.message(Command(commands=["dynamic"]))
async def dynamic(message: Message):
    await message.answer("Нажмите на кнопку ниже, чтобы показать больше опций.", reply_markup=start_keyboard)

@dp.callback_query()
async def handle_callback(callback_query: CallbackQuery):
    if callback_query.data == "show_more":
        # Заменяем кнопку "Показать больше" на новые кнопки
        await callback_query.message.edit_reply_markup(reply_markup=dynamic_keyboard)
    elif callback_query.data == "option_1":
        await callback_query.message.answer("Вы выбрали Опция 1!")
    elif callback_query.data == "option_2":
        await callback_query.message.answer("Вы выбрали Опция 2!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
