from aiogram.types import Message
from aiogram import Bot

from single_bot_hakaton.core_s.keyboards.reply import reply_main, reply_create, reply_repair
from single_bot_hakaton.core_s.keyboards.inline import inline_yn

f = False


async def get_start(message: Message, bot: Bot):
    await message.answer('Привет, я бот, который поможет тебе разобраться с документами, '
                         'получить поддержку или помощь от менеджера команды "Лидеры России - Москва", '
                         'а также принять заявку на опубликования искусства на сайте все СВОи! '
                         'Что делаете сделать?', reply_markup=reply_main())
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker="CAACAgIAAxkBAAINjWf122A5PqQJsk5JLgciJm9ORv0WAAI4bQAC8s-wSwH1_bdB_63FNgQ")


async def get_info(message: Message, bot: Bot):
    global f
    if message.text == 'Поделиться своим творчеством':
        await message.answer('Мы поможем распространить ваше творчество по всей России. '
                             'Для этого вам нужно перевести файл в pdf формат и отправить его нам. '
                             'Если вы хотите направить стихи, то запишите их ниже:')
    elif message.text == 'Создать документы':
        await message.answer('Хочешь создать паспорт, снилс и инн, '
                             'военный билет, водительские права и не знаешь, что делать? \n'
                             'Переходи на сайт: http://svo.meronor.ru '
                             'Если тут нет документа, который тебе нужен, '
                             'или ты хочешь получить помощь в оформлении, '
                             'жми: Мне нужна помощь', reply_markup=reply_create())
    elif message.text == 'Восстановить документы' or message.text == 'Создать':
        await message.answer('Потерял паспорт, снилс и инн,военный билет, '
                             'водительские права и не знаешь, что делать? '
                             'Переходи на сайт: http://svo.meronor.ru '
                             'Если тут нет документа который тебе нужен, '
                             'или ты хочешь получить помощь в оформлении, '
                             'жми : Мне нужна помощь', reply_markup=reply_repair())
    elif message.text == 'Понял, спасибо':
        await message.answer('Всегда пожалуйста, обращайтесь!', reply_markup=reply_main())
        await bot.send_sticker(
            chat_id=message.chat.id, sticker="CAACAgIAAxkBAAIM9Gf1sNXDTGV_rH4eZGsb_3URPEc5AAL_bAAC8s-wS1FDmB3RaEbpNgQ")
    elif message.text in ['Связь с менеджером', 'Мне нужна помощь']:
        if not message.from_user.username:
            await message.answer("Вы скрыли username в настройках Telegram! Напишите нам ваш номер или user_id")
        else:
            await message.answer('Мы свяжемся с вами в ближайшее время!', reply_markup=reply_main())
            await bot.send_message(chat_id=-1002345734770, text=f"Новая заявка на помощь "
                                                                f"@{message.from_user.username}",
                                   reply_markup=inline_yn(message.from_user.username))

    if f:
        f = False
        await bot.send_message(chat_id=-1002345734770, text=f'{message.text}\n@{message.from_user.username}')
        await message.answer("Спасибо, мы обрабатываем ваш запрос! Скоро ваше творчество появится на сайте!")
    elif message.text == 'Поделиться своим творчеством':
        f = True
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker="CAACAgIAAxkBAAIK82fzu-tM_sknVm6-M8BDIbyir8beAAIzbgACcAKhSzqBlL5pI8reNgQ")


async def get_delete(message: Message):
    await message.delete()
