from aiogram import Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import DEFAULT_LANGUAGE

import os

router = Router()

# 🔐 Временно жёсткий путь к языковому файлу (чтобы всё исключить)
lang_file_path = r"C:\Users\User\Desktop\KlikkyDeals\klikkydeals_final_full_project\klikkydeals_complete_clean\locales\en.py"
print("📂 Путь к языковому файлу:", lang_file_path)

lang_globals = {}
with open(lang_file_path, "r", encoding="utf-8") as f:
    exec(f.read(), lang_globals)

messages = lang_globals["messages"]

@router.callback_query(lambda c: c.data.startswith("cat_"))
async def category_selected(callback: types.CallbackQuery):
    category = callback.data.split("_")[1]
    await callback.message.answer(f"{messages['category_selected']} {category}")
    await callback.answer()
from aiogram import types, Router
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(lambda c: c.data == "aviatickets")
async def show_aviatickets(callback: types.CallbackQuery):
    # Загружаем локальное изображение из папки assets
    photo = FSInputFile("assets/flight_offer.png")

    # Текст с предложениями
    text = (
        "<b>🌟 Лучшие авиабилеты Европы!</b>\n\n"
        "✈️ Ницца → Милан — всего <b>39€</b>!\nДаты: <i>12–15 мая</i>\n\n"
        "✈️ Париж → Барселона — всего <b>45€</b>!\nДаты: <i>20–24 мая</i>\n\n"
        "✈️ Берлин → Рим — всего <b>55€</b>!\nДаты: <i>5–9 июня</i>\n\n"
        "✈️ Вена → Амстердам — всего <b>60€</b>!\nДаты: <i>18–22 июня</i>\n\n"
        "✈️ Мюнхен → Прага — всего <b>30€</b>!\nДаты: <i>2–5 июля</i>"
    )

    # Кнопка "Посмотреть предложения"
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔎 Посмотреть предложения",
                    url="https://www.example.com"
                )
            ]
        ]
    )

    # Отправляем сообщение
    await callback.message.answer_photo(
        photo=photo,
        caption=text,
        parse_mode="HTML",
        reply_markup=keyboard
    )
    await callback.answer()
