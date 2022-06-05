from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='📲 Onlayn ariza'),
            KeyboardButton(text='📔 Mahsulot katalogi'),
        ],
        [
            KeyboardButton(text='🔥 Sotuvda mavjud avtomobillar'),
            KeyboardButton(text='🎁 Chegirmalar'),
        ],
        [
            KeyboardButton(text='🔎 Mahsulotlar'),
            KeyboardButton(text="📋 Narxlar ro'yxati"),
            KeyboardButton(text='🏪 Dillerlik markazlari'),
        ],
        [
            KeyboardButton(text='🏢 Kompaniya haqida'),
            KeyboardButton(text="📞 Bog'lanish uchun"),
        ],
        [
            KeyboardButton(text='🌐 Tilni tanlash'), # TilKeyboard
        ],
    ],
    resize_keyboard=True
)




# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#
# menu = ReplyKeyboardMarkup(
#     keyboard = [
#         [
#             KeyboardButton(text='📲 Онлайн заявка'),
#             KeyboardButton(text='📔 Каталог продукции'),
#         ],
#         [
#             KeyboardButton(text='🔥 Автомобили в наличии'),
#             KeyboardButton(text='🎁 Текущие акции компании'),
#         ],
#         [
#             KeyboardButton(text='🔎 Продукция'),
#             KeyboardButton(text='📋 Прайс-лист'),
#             KeyboardButton(text='🏪 Дилерские центры'),
#         ],
#         [
#             KeyboardButton(text='🏢 О компании'),
#             KeyboardButton(text='📞 Контакты'),
#         ],
#         [
#             KeyboardButton(text='🌐 Изменить язык'),
#         ],
#     ],
#     resize_keyboard=True
# )