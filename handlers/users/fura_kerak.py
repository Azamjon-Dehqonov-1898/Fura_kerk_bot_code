from data.config import adminlar, kanallar
from states.fura_kerak_holat import Forma2
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from keyboards.default.viloyatlar import viloyat
from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from aiogram.types import CallbackQuery, Message, message
from keyboards.default.ha_Yoq import ha
from keyboards.default.asosiy import asosiy
from keyboards.default.kontakt import tel
from keyboards.default.viloyatlar_kerak import viloyat_kerak
from keyboards.default.kanalga_ulashish_kerak import kanal_ulashish_kerak
lugat1 = {}


@dp.message_handler(state=Forma2.Tur_qabul_qlish2)
async def tara(malumot: Message):
    tur= malumot.text
    lugat1['🚛Tur:'] = tur
    await malumot.answer(text="Bog'lanish uchun telefon no'mer?",reply_markup=tel)
    await Forma2.Aloqa_qabul_qlish2.set()


@dp.message_handler(state=Forma2.Aloqa_qabul_qlish2,content_types=ContentTypes.CONTACT)
async def ism_uchun(malumot: Message):
    tel = malumot.contact.phone_number
    print(tel)
    lugat1['📞Aloqa:'] ='+' + tel
    user = malumot.from_user.username
    if user:
        lugat1['📱Telegram:'] = '@' + user
    else:
        fris = malumot.from_user.first_name
        lugat1['📱Telegram:'] = fris
    await malumot.answer(text='Fura Qaysi hududda kerak ?',reply_markup=viloyat_kerak)
    await Forma2.Hudud_qabul_qlish2.set()

@dp.message_handler(state=Forma2.Aloqa_qabul_qlish2)
async def tara(malumot: Message):
    user = malumot.from_user.username
    if user:
        lugat1['📱Telegram:'] = '@' + user
    else:
        fris = malumot.from_user.first_name
        lugat1['📱Telegram:'] = fris
    tel = malumot.text
    tel = tel.strip()
    davlat = tel[0:4]
    kod = tel[4:6]
    raqam = tel[6:]
    kodlar = [33,93,94,95,99,97,55,90,98,91,88,97,]
    if davlat != '+998':
        await malumot.answer(text='+998YYXXXXXXX formatda telefon raqamingizni kiriting')
    elif not int(kod) in kodlar:
        await malumot.answer(text=f"{kod} bunday kodli raqam mavjud emas")
    elif len(raqam) != 7:
        await malumot.answer(text=f"{raqam} da xatolik bor")
    elif davlat == '+998' and int(kod) in kodlar and len(raqam)==7:
        lugat1['📞Aloqa:'] = tel
        await malumot.answer(text='Hozir qayerda ekaningiz,(Turgan joyingiz manzili)', reply_markup=viloyat)
    await Forma2.Hudud_qabul_qlish2.set()


@dp.message_handler(state=Forma2.Hudud_qabul_qlish2)
async def ism_uchun(malumot: Message, state: FSMContext):
    joy = malumot.text
    lugat1['🌐Hudud:'] = joy + " " + "viloyatida"
    matn1: str = "#Bo'sh_fura_kerak \n\n"
    for a in lugat1:
        matn1 += a + lugat1[a] + '\n'
    await Forma2.tasdiqlash2.set()
    await malumot.answer(text=matn1)
    await malumot.answer(text="Malumotlaringiz to'g'rmi ?",reply_markup=ha)


@dp.message_handler(text='Ha',state=Forma2.tasdiqlash2)
async def bot_echo(message: types.Message,state:FSMContext):
    foydalanuvchi = message.from_user.first_name
    await message.answer(text='Malumotlaringiz adminga yuborildi',reply_markup=asosiy)
    matn1: str = "#Bo'sh_fura_kerak \n\n"
    for a in lugat1:
        matn1 += a + lugat1[a] + '\n'
    await bot.send_message(chat_id=kanallar[0],text=matn1)
    await state.finish()
#
# @dp.message_handler(text='Kanalga_Ulashish',user_id=adminlar[0])
# async def tara(malumot: Message):
#     matn1: str = "#Bo'sh_fura_kerak \n\n"
#     for a in lugat1:
#         matn1 += a + lugat1[a] + '\n'
#
#     for k in kanallar:
#         await bot.send_message(chat_id=k,text=matn1,reply_markup=asosiy)


@dp.message_handler(text="Yo'q",state=Forma2.tasdiqlash2)
async def bot_echo(message: types.Message,state:FSMContext):
    foydalanuvchi = message.from_user.first_name
    await message.answer(text='Malumotlaringiz boshqatdan kiriting?',reply_markup=asosiy)
    await state.finish()



