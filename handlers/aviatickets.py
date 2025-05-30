from aiogram import types, Router
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.callback_query(lambda c: c.data == "aviatickets")
async def show_aviatickets(callback: types.CallbackQuery):
    # Загружаем локальное изображение из папки assets
    photo = FSInputFile("assets/flight_offer.png")

    # Текст описания к карточке
    text = (
        "<b>🌟 Лучшие авиабилеты Европы!</b>\n\n"
        "✈️ Ницца → Милан - всего 39€! Даты: 12–15 мая\n"
        "✈️ Париж → Барселона - всего 45€! Даты: 20–24 мая\n"
        "✈️ Берлин → Рим - всего 55€! Даты: 5–9 июня\n"
        "✈️ Вена → Амстердам - всего 60€! Даты: 18–22 июня\n"
        "✈️ Мюнхен → Прага - всего 30€! Даты: 2–5 июля"
    )

    # Кнопка для перехода
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔎 Посмотреть предложения", url="https://www.example.com")]
    ])

    # Отправляем карточку с фото и кнопкой
    await callback.message.answer_photo(
        photo=photo,
        caption=text,
        parse_mode="HTML",
        reply_markup=keyboard
    )
    await callback.answer()