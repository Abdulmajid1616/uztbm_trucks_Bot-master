from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.ArizaKeyboard import menuAriza
from keyboards.default.AvtosamosvalKeyboard import menuAvtosamosval
from keyboards.default.HududKeyboard import menuHudud
from keyboards.default.MahsulotKeyboard import menuMahsulot
from keyboards.default.Surxandarinskaya import menuSurxandarinskaya
from keyboards.default.menuKeyboard import menu
from keyboards.default.TilKeyboard import menuTil

from loader import dp # <b></b>

# @dp.message_handler(Command("menu"))
# async def show_menu(message: Message):
#     await message.answer("Kurslarni tanlang", reply_markup=menu)

# @dp.message_handler(text='')
# async def send_link(message: Message):
#     await message.answer("")
# Mukammal Telegram bot kursi: https://mohirdev.uz/courses/telegram
 # 🌐 Tilni tanlash

@dp.message_handler(text='🌐 Tilni tanlash')
async def send_link(message: Message):
    await message.reply("🇺🇿 Kerakli tilni tanlang \n\n 🇷🇺 Выберите нужный язык", reply_markup=menuTil)

@dp.message_handler(text="📞 Bog'lanish uchun")
async def send_link(message: Message):
    await message.answer("Юридический адрес:\n Республика Узбекистан,\n Самаркандская область,\n Джамбайский район, 140400,\n ул. Ташкентская,\n\n 2 Ташкентский офис: \nРеспублика Узбекистан, г. Ташкент, \n100047, Мирабадский район\n ул. Амира Темура, 13\n\n 📞Телефон: +998 78 148 80 80\n✉️E-mail: info@man.uz,\n web: www.uztbm.uz")

@dp.message_handler(text="🇺🇿 O'zbek tili")
async def send_link(message: Message):
    await message.answer("🏡 Bosh menu", reply_markup=menu)

@dp.message_handler(text="🇷🇺 Русский язык")
async def send_link(message: Message):
    await message.answer("🏡 Главное меню", reply_markup=menu)

@dp.message_handler(text="🏢 Kompaniya haqida")
async def send_link(message: Message):
    await message.answer("СП ООО «UZ TRUCK AND BUS  MOTORS» - является производителем большегрузной и пассажирской техники MAN и Sinotruk в Центрально- азиатском регионе. Предприятие основано в августе 2009 года и расположено в Самаркандской области.Совместное узбекско-германское-китайское предприятие «UZ TRUCK AND BUS MOTORS» производит современную и надежную коммерческую технику MAN и Sinotruk грузоподъемностью от 5 до 70 тонн. УчредителиАО «Узавтосаноат» - 34% (Узбекистан)«MAN Truck & Bus AG» - 33% (Германия)Sinotruk International Investment Ltd. - 33% (КНР)Уставный капитал - 32,8 млн.евро.Продукция:Седельные тягачи, самосвалы, спецтехника, фургоны, городские и междугородные автобусы. Модельный ряд грузовой и спецтехники составляет более 60 позиций.")

@dp.message_handler(text="🏪 Dillerlik markazlari")
async def send_link(message: Message):
    await message.reply("Iltimos, quyida keltirilgan <b>hududlardan</b> birini tanlang")

@dp.message_handler(text="📋 Narxlar ro'yxati")
async def send_link(message: Message):
    await message.answer("⏰ 2021-07-27 16:56:52")

@dp.message_handler(text="🔎 Mahsulotlar")
async def send_link(message: Message):
    await message.reply("Quyida keltirilgan <b>mahsulot</b> turlaridan birini tanlang")

@dp.message_handler(text="🎁 Chegirmalar")
async def send_link(message: Message):
    await message.answer("Хотите получить свою технику сразу, без ожидания и очередей? Тогда торопитесь – Uz Truck & Bus Motors представляет вам эту возможность!На данный момент на складе готовой продукции компании в наличие имеется следующая техника, которую вы можете получить сразу после оплаты контракта. Цены на продукцию вы можете уточнить у ближайшего дилера.Не упустите свой шанс, звоните прямо сейчас.Телефон для справок: +99878 148-80-80")
    await message.answer("Друзья!Компания Uz Truck & Bus Motors желает вам и вашим близким здоровья!Мы благодарим вас за вашу сознательность и поэтому специально для тех, кто сидит дома предлагаем услуги бесконтактного заключения договоров на всю технику компании.Для того, чтобы получить информацию по заключению договора, свяжитесь пожалуйста с нашими региональными менеджерами через единый call-центр 78 148 80 80. Наши менеджеры с удовольствием предоставят вам всю необходимую информацию, а также отправят полное описание нашей техники и прайс на вашу электронную почту. После уточнения деталей, вам будет предоставлен электронный вариант договора.На официальном сайте компании покупатели также могут ознакомиться с ассортиментом техники в наличии. Оплатить по договору покупатели могут в любом из филиалов банка. Для вашего удобства, оригинал договора можно забрать уже при получении вашей техники, согласно срокам поставки.Берегите себя и своих близких и будьте здоровы!")

@dp.message_handler(text="🔥 Sotuvda mavjud avtomobillar")
async def send_link(message: Message):
    await message.answer("")

@dp.message_handler(text="📔 Mahsulot katalogi")
async def send_link(message: Message):
    await message.answer("⏰ 2021-05-18 17:23:31")

@dp.message_handler(text="📲 Onlayn ariza")
async def send_link(message: Message):
    await message.reply("Quyida keltirilgan <b>ariza</b> turlaridan birini tanlang", reply_markup=menuAriza)

@dp.message_handler(text="🚌 Mahsulotlar")
async def send_link(message: Message):
    await message.reply("Quyida keltirilgan <b>mahsulot</b> turlaridan birini tanlang", reply_markup=menuMahsulot)

@dp.message_handler(text="Автосамосвалы")
async def send_link(message: Message):
    await message.reply("Quyida keltirilgan <b>mahsulot</b> turlaridan birini tanlang", reply_markup=menuAvtosamosval)

@dp.message_handler(text="MAN CLA 31.280 6x4 18 тонн")
async def send_link(message: Message):
    await message.reply("Iltimos, quyida keltirilgan <b>hududlardan</b> birini tanlang", reply_markup=menuHudud)

@dp.message_handler(text="Сурхандарьинская область")
async def send_link(message: Message):
    await message.reply("Kerakli <b>dillerlik</b> markazini tanlang", reply_markup=menuSurxandarinskaya)

@dp.message_handler(text="")
async def send_link(message: Message):
    await message.answer()

@dp.message_handler(text="")
async def send_link(message: Message):
    await message.answer()

@dp.message_handler(text="")
async def send_link(message: Message):
    await message.answer()

@dp.message_handler(text="")
async def send_link(message: Message):
    await message.answer()




 # "Mavzu tanlang", reply_markup=menuPython
# "https://python.sariq.dev", reply_markup=ReplyKeyboardRemove()

@dp.message_handler(text='Boshiga')
async def send_link(message: Message):
    await message.answer("🏡 Bosh menu", reply_markup=menu)