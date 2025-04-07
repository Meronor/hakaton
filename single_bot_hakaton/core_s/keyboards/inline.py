from aiogram.utils.keyboard import InlineKeyboardBuilder


def inline_yn():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='Yes', callback_data='Y')
    keyboard_builder.button(text='No', callback_data='N')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
