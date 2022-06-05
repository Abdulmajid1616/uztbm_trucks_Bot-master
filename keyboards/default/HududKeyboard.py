from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuHudud = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сурхандарьинская область"),
            KeyboardButton(text="Город Ташкент"),
        ],
        [
            KeyboardButton(text="Ташкентская область"),
            KeyboardButton(text="Ферганская область"),
        ],
        [
            KeyboardButton(text="Хорезмская область"),
            KeyboardButton(text="Бухарская область"),
        ],
        [
            KeyboardButton(text="Наманганская область"),
            KeyboardButton(text="Джизакская область"),
        ],
        [
            KeyboardButton(text="Навоийская область"),
            KeyboardButton(text="Андижанская область"),
        ],
        [
            KeyboardButton(text="Кашкадарьинская область"),
            KeyboardButton(text="Самаркандская область"),
        ],
        [
            KeyboardButton(text="🔙 Orqaga"),
        ],
    ],
    resize_keyboard=True
)