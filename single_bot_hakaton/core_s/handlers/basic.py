from aiogram.types import Message
from aiogram import Bot
from core_s.keyboards.reply import reply_main, reply_docs, reply_yn, reply_catch
# from single_bot.core_s.keyboards.inline import inline_yn

f = False

async def get_start(message: Message, bot: Bot):
    await message.answer('*Приветствие*', reply_markup=reply_main())
    # with open('123.png', 'rb') as photo_file:
    #    await bot.send_photo(chat_id=message.chat.id, photo=photo_file)
    await bot.send_sticker(
        chat_id=message.chat.id,
        sticker="CAACAgIAAxkBAAIK82fzu-tM_sknVm6-M8BDIbyir8beAAIzbgACcAKhSzqBlL5pI8reNgQ"  # подставьте реальный file_id
    )


async def get_info(message: Message, bot: Bot):
    global f
    if message.text == 'Поделиться своим искусством':
        await message.answer('Мы поможем распространить ваше искусство;)')
    elif message.text == 'Связь с человеком':
        await message.answer('Можете задать любой вопрос')
    elif message.text == 'Помощь с документами':
        await message.answer('Что именно вас интересует?', reply_markup=reply_docs())
    elif message.text == 'Восстановить' or message.text == 'Создать':
        await message.answer('Согласны ли вы на обработку персональных данных?', reply_markup=reply_yn())
    elif message.text == 'Собрать пакет документов':
        await message.answer('Какие именно документы вас интересуют?', reply_markup=reply_catch())
    elif message.text == 'Другое':
        await message.answer('Мы свяжемся с вами в ближайшем будущем!', reply_markup=reply_main())


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
