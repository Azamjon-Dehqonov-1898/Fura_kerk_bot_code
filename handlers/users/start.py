from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.shaxsiy import Shaxsiy
from loader import dp
from states.fura_kerak_holat import Forma2
from states.fura_bor_holat import Forma
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import types
from aiogram.types import CallbackQuery, Message,message
from keyboards.default.asosiy import asosiy
from loader import dp,data_base
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.tur import Tur

@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    if username==None:
        username="username yo'q"
    idd = data_base.select_users_ids()
    d = (max(idd))
    id = d[0]+1
    try:
        data_base.user_qoshish(id=id,user_id=user_id,username=username)
    except Exception as xato:
        print(xato)
    foydalanuvchi = message.from_user.first_name
    await message.answer(text=f"Assalomu alaykum {foydalanuvchi} kerakli bo'limni tallang?",reply_markup=asosiy)


@dp.message_handler(text='Fura kerak')
async def bot_echo(message: types.Message):
    foydalanuvchi = message.from_user.first_name
    await message.answer(text=f"Asalomu alaykum,{foydalanuvchi}, Sizga  "
                              f" Fura topishingizga yordam beramiz,"
                              f"Iltmos Sizga qanday Fura kerak ?",reply_markup=Tur)
    await Forma2.Tur_qabul_qlish2.set()



@dp.message_handler(text="Fura bor")
async def bot_echo(message: types.Message):
    foydalanuvchi = message.from_user.first_name
    await message.answer(text=f"Asalomu alaykum,{foydalanuvchi}, Sizga  "
                              f" yuk topishingizga yordam beramiz,"
                              f"Sizda qanday Fura bor ?",reply_markup=Tur)
    await Forma.Tur_qabul_qlish.set()


