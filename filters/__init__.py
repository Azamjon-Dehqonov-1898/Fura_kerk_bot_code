from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter


if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    pass
from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from  .shaxsiy import Shaxsiy
from .kanal import Kanal
from .guruh import Gurux

if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    pass
    dp.filters_factory.bind(Gurux)
    dp.filters_factory.bind(Kanal)
    dp.filters_factory.bind(Shaxsiy)
