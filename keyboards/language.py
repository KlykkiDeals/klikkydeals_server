from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def language_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")],
        [InlineKeyboardButton(text="🇫🇷 Français", callback_data="lang_fr")],
        [InlineKeyboardButton(text="🇩🇪 Deutsch", callback_data="lang_de")],
        [InlineKeyboardButton(text="🇪🇸 Español", callback_data="lang_es")],
        [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
    ])
