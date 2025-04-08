from aiogram.filters.callback_data import CallbackData


class SubsInfo(CallbackData, prefix='mac'):
    during: str
    cost: int
    stage: int
    days: int


class accept(CallbackData, prefix='mac'):
    username: str
    stage: int
