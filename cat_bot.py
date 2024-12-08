import asyncio
import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN, CAT_API_KEY
from googletrans import Translator

bot = Bot(token=TOKEN)
dp = Dispatcher()

translator = Translator()  # Создаем экземпляр переводчика


# Функция для получения списка пород кошек
def get_cat_breeds():
    url = "https://api.thecatapi.com/v1/breeds"
    headers = {"x-api-key": CAT_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()


# Функция для получения картинки кошки по породе
def get_cat_image_by_breed(breed_id):
    url = f"https://api.thecatapi.com/v1/images/search?breed_ids={breed_id}"
    headers = {"x-api-key": CAT_API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]['url'] if data else None


# Функция для получения информации о породе кошек
def get_breed_info(breed_name):
    breeds = get_cat_breeds()
    for breed in breeds:
        if breed_name.lower() in (breed['name'].lower(), breed.get('alt_names', '').lower()):
            return breed
    return None


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Напиши мне породу кошки, и я пришлю её фото и описание.")


@dp.message()
async def send_cat_info(message: Message):
    breed_name = message.text.strip()
    breed_info = get_breed_info(breed_name)
    if breed_info:
        cat_image_url = get_cat_image_by_breed(breed_info['id'])

        # Перевод текста с английского на русский
        translated_name = translator.translate(breed_info['name'], src='en', dest='ru').text
        translated_origin = translator.translate(breed_info['origin'], src='en', dest='ru').text
        translated_description = translator.translate(breed_info['description'], src='en', dest='ru').text
        translated_temperament = translator.translate(breed_info['temperament'], src='en', dest='ru').text
        translated_life_span = translator.translate(f"{breed_info['life_span']} years", src='en', dest='ru').text

        info = (
            f"Порода: {translated_name}\n"
            f"Происхождение: {translated_origin}\n"
            f"Описание: {translated_description}\n"
            f"Характер: {translated_temperament}\n"
            f"Продолжительность жизни: {translated_life_span}"
        )
        if cat_image_url:
            await message.answer_photo(photo=cat_image_url, caption=info)
        else:
            await message.answer(info)
    else:
        await message.answer("Порода не найдена. Попробуйте ввести название породы на русском языке.")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
