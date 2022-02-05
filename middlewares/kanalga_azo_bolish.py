from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from data.config import kanallar
from utils import azolikni_tekshrish
from loader import bot
from utils.azolikni_tekshrish import tekshrish


class Asosiy_cheking(BaseMiddleware):
    async def on_pre_process_update(self, xabar:types.Update, data:dict,):
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return
        matn = "Quydagi Kanalga azo bo'ling,Keyin Botdan foydalanishingiz mumkin\n"


        daslabki_holati = True
        for k in kanallar:
            holat = await tekshrish(user_id=user_id,kanal_link=k)
            daslabki_holati *= holat

            kanal= await bot.get_chat(k)
            if not holat:
                link = await kanal.export_invite_link()
                matn += (f"👉 <a href='{link}'>{kanal.title}</a>\n")
        if not daslabki_holati:
            await xabar.message.answer(matn,disable_web_page_preview=True,)
            raise CancelHandler()
