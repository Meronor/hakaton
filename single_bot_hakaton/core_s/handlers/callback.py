from aiogram.types import CallbackQuery
from single_bot_hakaton.core_s.handlers.basic import get_delete
from single_bot_hakaton.core_s.utils.CallbackData import accept


async def acception(call: CallbackQuery, callback_data: accept):
    user = call.from_user

    await call.message.answer(f" @{user.username if user.username else 'нет'} cвяжитесь с @{callback_data.username}")
    await call.bot.send_message(chat_id=user.id, text=f"Cвяжитесь с @{callback_data.username}")
    await get_delete(call.message)
    await call.answer()
