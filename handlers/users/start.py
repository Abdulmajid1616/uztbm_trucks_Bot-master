from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menuKeyboard import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # await message.answer(f"Salom, {message.from_user.full_name}!")
    # await message.answer("🏡 Главное меню", reply_markup=menu)
    await message.answer("🏡 Bosh menu", reply_markup=menu)
