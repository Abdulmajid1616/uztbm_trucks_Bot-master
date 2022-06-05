from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuTil = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbek tili"),
            KeyboardButton(text="🇷🇺 Русский язык"),
        ],
        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Boshiga"),
        ],
    ],
    resize_keyboard=True
)