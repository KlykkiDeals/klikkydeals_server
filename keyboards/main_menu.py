from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard(categories: list[str]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=categories[0], callback_data="aviatickets")],
            *[
                [InlineKeyboardButton(text=cat, callback_data=f"cat_{i}")]
                for i, cat in enumerate(categories[1:], start=1)
            ]
        ]
    )
