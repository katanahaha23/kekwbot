import asyncio
from distutils.dep_util import newer
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
import logging
from aiogram import Bot, Dispatcher, types 



# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7053088731:AAFgdmKAZ643ZuyYddEIOOGB5ckt9TdEEMU")
# Диспетчер
dp = Dispatcher()

# chan_id = -1002072999477


@dp.message(Command["start"])
async def cmd_start(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=-1002072999477, user_id=message.from_user.id)
    if user_channel_status["status"] != 'left':
        pass
        await bot.send_message(message.from_user.id, 'text if in group')
    else:
        await bot.send_message(message.from_user.id, 'text if not in group')

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())