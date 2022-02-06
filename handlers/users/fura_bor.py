from data.config import adminlar, kanallar
from keyboards.default.kontakt import tel
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from loader import dp
from keyboards.default.asosiy import asosiy
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from aiogram.types import CallbackQuery, Message, message
from states.fura_bor_holat import Forma
from loader import dp
from keyboards.default.viloyatlar import viloyat
from keyboards.default.ha_Yoq import ha
from keyboards.default.lokatsiya import joylashuv
from keyboards.default.kanalga_ulashish import kanal_ulashish
from loader import bot
from keyboards.inline.kanalga_ulashish import inline_kanal
lugat = {}



@dp.message_handler(state=Forma.Tur_qabul_qlish)
async def tara(malumot: Message):
    tur = malumot.text
    lugat['🚛Tur:'] = tur
    await malumot.answer(text="Bog'lanish uchun telefon no'mer?", reply_markup=tel)
    await Forma.Aloqa_qabul_qlish.set()


@dp.message_handler(state=Forma.Aloqa_qabul_qlish,content_types=ContentTypes.CONTACT)
async def ism_uchun(malumot: Message):
    tel = malumot.contact.phone_number
    print(tel)
    lugat['📞Aloqa:'] ='+' + tel
    user = malumot.from_user.username
    if user:
        lugat['📱Telegram:'] = '@' + user
    else:
        fris = malumot.from_user.first_name
        lugat['📱Telegram:'] = fris
    await malumot.answer(text='Hozir qayerda ekaningiz,(Turgan joyingiz manzili)',reply_markup=viloyat)
    await Forma.Hudud_qabul_qlish.set()

@dp.message_handler(state=Forma.Aloqa_qabul_qlish)
async def tara(malumot: Message):
    user = malumot.from_user.username
    if user:
        lugat['📱Telegram:'] = '@' + user
    else:
        fris = malumot.from_user.first_name
        lugat['📱Telegram:'] = fris
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
        lugat['📞Aloqa:'] = tel
        await malumot.answer(text='Hozir qayerda ekaningiz,(Turgan joyingiz manzili)', reply_markup=viloyat)
    await Forma.Hudud_qabul_qlish.set()

@dp.message_handler(state=Forma.Hudud_qabul_qlish)
async def ism_uchun(malumot: Message, state: FSMContext):
    joy = malumot.text
    lugat['🌐Hudud:'] = joy
    matn: str = "#Bo'sh_fura_bor \n\n"
    for i in lugat:
        matn += i + lugat[i]  + '\n'

    await Forma.tasdiqlash.set()
    await malumot.answer(text=matn)
    await malumot.answer(text="Malumotlaringiz to'g'rmi ?", reply_markup=ha)

@dp.message_handler(text='Ha',state=Forma.tasdiqlash)
async def bot_echo(message: types.Message,state:FSMContext):
    foydalanuvchi = message.from_user.first_name
    await message.answer(text='Malumotlaringiz adminga yuborildi',reply_markup=asosiy)
    matn: str = "#Bo'sh_fura_bor \n\n"
    for i in lugat:
        matn += i + lugat[i] + '\n'
    await bot.send_message(chat_id=kanallar[0],text=matn)
    await state.finish()

 @dp.message_handler(text='Kanalga Ulashish',user_id=adminlar[0])
 async def tara(malumot: Message):
     matn: str = "#Bo'sh_fura_bor \n\n"
     for i in lugat:
         matn += i + lugat[i] + '\n'

     for k in kanallar:
         await bot.send_message(chat_id=k,text=matn,,reply_markup=kanal_ulashish)





@dp.message_handler(text="Yo'q",state=Forma.tasdiqlash)
async def bot_echo(message: types.Message,state:FSMContext):
    foydalanuvchi = message.from_user.first_name
    await message.answer(text='Malumotlaringiz boshqatdan kiriting?',reply_markup=asosiy)
    await state.finish()




