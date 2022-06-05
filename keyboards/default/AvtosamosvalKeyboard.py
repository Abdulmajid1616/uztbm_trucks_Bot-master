from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuAvtosamosval = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="MAN CLA 31.280 6x4 18 тонн"),
            KeyboardButton(text="TGS 40.400 6х4 BB 25 тонн"),
        ],
        [
            KeyboardButton(text="MAN TGS 41.400 8x4 30 тонн"),
            KeyboardButton(text="MAN TGS 33.400 6X4 BB 20 тонн"),
        ],
        [
            KeyboardButton(text="Sinotruk Golden Prince 25 тонн"),
            KeyboardButton(text="🔙 Orqaga"),
        ],
    ],
    resize_keyboard=True
)