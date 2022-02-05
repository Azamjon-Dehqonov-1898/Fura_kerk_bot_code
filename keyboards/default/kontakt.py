from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
tel = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='KONTAKT ULASHISH',request_contact=True)
        ]
    ],
    resize_keyboard=True
)