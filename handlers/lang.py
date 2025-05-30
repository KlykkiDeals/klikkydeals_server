from aiogram import Router, types
from keyboards.main_menu import main_menu_keyboard

import importlib

router = Router()

@router.callback_query(lambda c: c.data.startswith("lang_"))
async def set_language(callback: types.CallbackQuery):
    lang_code = callback.data.split("_")[1]

    try:
        # Динамически импортируем нужный языковой файл
        locale = importlib.import_module(f"locales.{lang_code}")
        messages = locale.messages
    except ModuleNotFoundError:
        await callback.message.answer("❌ Language not supported.")
        await callback.answer()
        return

    await callback.message.answer(
        messages["welcome"],
        reply_markup=main_menu_keyboard(messages["categories"])
    )
    await callback.answer()
