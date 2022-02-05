from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

inline_kanal = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kanalga Ulashish",callback_data='kanall')
        ]
    ]
)