from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuMahsulot = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Автосамосвалы"),
            KeyboardButton(text="Автобусы"),
        ],
        [
            KeyboardButton(text="Седельные тягачи"),
            KeyboardButton(text="Автофургоны"),
        ],
        [
            KeyboardButton(text="Специальная техника"),
            KeyboardButton(text="🔙 Orqaga"),
        ],
    ],
    resize_keyboard=True
)