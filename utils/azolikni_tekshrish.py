from typing import Union

from aiogram import Bot


async def tekshrish(user_id,kanal_link:Union[str]):
    bot = Bot.get_current()
    azo = await bot.get_chat_member(user_id=user_id,chat_id=kanal_link)
    return azo.is_chat_member()

