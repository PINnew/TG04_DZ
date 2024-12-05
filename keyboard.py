from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Тестовая кнопка 1")],
   [KeyboardButton(text="Тестовая кнопка 2"), KeyboardButton(text="Тестовая кнопка 3")]
], resize_keyboard=True)

inline_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Видео", url="https://www.youtube.com/")]
])


#url_button = InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/")
#keyboard = InlineKeyboardMarkup().add(url_button)
