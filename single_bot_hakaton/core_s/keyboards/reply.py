from aiogram.utils.keyboard import ReplyKeyboardBuilder


def reply_main():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Восстановить документы')
    keyboard_builder.button(text='Создать документы')
    keyboard_builder.button(text='Связь с менеджером')
    keyboard_builder.button(text='Поделиться своим творчеством')
    keyboard_builder.adjust(2, 2)
    return keyboard_builder.as_markup(resize_keyboard=True)

def reply_create():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Понял, спасибо')
    keyboard_builder.button(text='Мне нужна помощь')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(resize_keyboard=True)

def reply_repair():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Понял, спасибо')
    keyboard_builder.button(text='Мне нужна помощь')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(resize_keyboard=True)
