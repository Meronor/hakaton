from aiogram.utils.keyboard import ReplyKeyboardBuilder


def reply_main2():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Выплаты участникам СВО')
    keyboard_builder.button(text='Психологическая помощь')
    keyboard_builder.button(text='Часто задаваемые вопросы')
    keyboard_builder.button(text='Навигация по москве')
    keyboard_builder.button(text='Связь с человеком')
    keyboard_builder.button(text='Творчество')
    keyboard_builder.adjust(1, 2, 3)
    return keyboard_builder.as_markup(resize_keyboard=True)

def reply_main():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Помощь с документами')
    keyboard_builder.button(text='Связь с человеком')
    keyboard_builder.button(text='Поделиться своим искусством')
    keyboard_builder.adjust(2, 1)
    return keyboard_builder.as_markup(resize_keyboard=True)

def reply_docs():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Восстановить документы')
    keyboard_builder.button(text='Создать документы')
    keyboard_builder.button(text='Собрать пакет документов')
    keyboard_builder.button(text='Другое')
    keyboard_builder.adjust(2, 1, 1)
    return keyboard_builder.as_markup(resize_keyboard=True)

def reply_yn():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Да')
    keyboard_builder.button(text='Нет')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(resize_keyboard=True)

def reply_catch():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Документы для выплат')
    keyboard_builder.button(text='Документы для подтверждения инвалидности')
    keyboard_builder.button(text='Другое')
    keyboard_builder.adjust(2, 1)
    return keyboard_builder.as_markup(resize_keyboard=True)