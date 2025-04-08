from aiogram.types import Message
from aiogram import Bot
from flask.cli import pass_script_info

from single_bot_hakaton.core_s.keyboards.reply import reply_main, reply_create, reply_repair
from single_bot_hakaton.core_s.keyboards.inline import inline_yn

f = False

async def get_start(message: Message, bot: Bot):
    await message.answer('*Приветствие*', reply_markup=reply_main())
    # with open('123.png', 'rb') as photo_file:
    #    await bot.send_photo(chat_id=message.chat.id, photo=photo_file)
    await bot.send_sticker(
        chat_id=message.chat.id,
        sticker="CAACAgIAAxkBAAIK82fzu-tM_sknVm6-M8BDIbyir8beAAIzbgACcAKhSzqBlL5pI8reNgQ")


async def get_info(message: Message, bot: Bot):
    global f
    if message.text == 'Поделиться своим творчеством':
        await message.answer('Мы поможем распространить ваше творчество')
    elif message.text == 'Создать документы':
        await message.answer('Текст', reply_markup=reply_create())
    elif message.text == 'Восстановить документы' or message.text == 'Создать':
        await message.answer('Текст', reply_markup=reply_repair())
    elif message.text == 'Понял, спасибо':
        await message.answer('Текст')
        await bot.send_sticker(
            chat_id=message.chat.id,sticker="CAACAgIAAxkBAAIM9Gf1sNXDTGV_rH4eZGsb_3URPEc5AAL_bAAC8s-wS1FDmB3RaEbpNgQ")
    elif message.text in ['Связь с менеджером', 'Мне нужна помощь'] :
        if not message.from_user.username:
            await message.answer("Вы скрыли username в настройках Telegram! Напишите нам ваш номер или user_id")
        else:
            await message.answer('Мы свяжемся с вами в ближайшее время!', reply_markup=reply_main())
            await bot.send_message(chat_id=-1002345734770, text=f"Новая заявка на помощь "
                            f"@{message.from_user.username}", reply_markup=inline_yn(message.from_user.username))


    if message.text  in ['Другое', 'Поделиться своим искусством'] and f:
        await bot.forward_message(
            chat_id=6790408576,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )
    elif message.text == 'Творчество':
        f = True
    else:
        f = False


async def get_delete(message: Message):
    await message.delete()
