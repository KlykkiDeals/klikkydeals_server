from aiogram import Router, types
from aiogram.filters.command import Command
from keyboards.lang_choice import language_keyboard
from locales import en

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "✨ <b>WELCOME TO KLIKKYDEALS</b> ✨\n\n"
        "🎁 <i>Your smart assistant to find the best deals, discounts, and hot offers from around the web.</i>\n\n"
        f"{en.messages['choose_lang']}",
        reply_markup=language_keyboard()
    )
