from aiogram.utils.keyboard import InlineKeyboardBuilder
from single_bot_hakaton.core_s.utils.CallbackData import accept


def inline_yn(username):
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='Принять', callback_data=accept(username=username, stage=1))
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
