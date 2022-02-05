from  aiogram.dispatcher.filters.state import State,StatesGroup


class Forma(StatesGroup):
    Tur_qabul_qlish = State()
    Aloqa_qabul_qlish = State()
    Hudud_qabul_qlish = State()
    tasdiqlash = State()