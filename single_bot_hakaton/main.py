import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from core_s.handlers.basic import get_start, get_info
from core_s.settings import settings
from core_s.utils.commands import set_commands
from aiogram import F

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def start_bot(bot: Bot):
    await set_commands(bot)


async def start():
    bot = Bot(token=settings.bots.bot_token)
    dp = Dispatcher()
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_info)

    await start_bot(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
