from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuAriza = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚌 Mahsulotlar"),
            KeyboardButton(text="🛠️ Xizmatlar"),
        ],
        [
            KeyboardButton(text="⚙️ Ehtiyot qismlari"),
            KeyboardButton(text="🚘 Test drive"),
        ],
        [
            KeyboardButton(text="🏡 Bosh menu")
        ],
    ],
    resize_keyboard=True
)