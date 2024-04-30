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

from aiogram.utils.formatting import Text, Bold



# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7053088731:AAFgdmKAZ643ZuyYddEIOOGB5ckt9TdEEMU")
# Диспетчер
dp = Dispatcher()

# chan_id = -1002072999477

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Отправка приветственного сообщения
    await message.reply("Добро пожаловать! Этот бот предназначен для работы с подпиской на канал")

    # Проверка подписки на канал
    channel = '-1002072999477'
    subscribed = await bot.get_chat_member(channel, message.from_user.id)
    if subscribed.status == 'left':
        await bot.send_message(chat_id=message.chat.id, text='Для работы с ботом необходимо подписаться на наш канал: https://t.me/{}'.format(channel), disable_web_page_preview=True)
    else:
        await bot.send_message(chat_id=message.chat.id, text='Ваш текущий баланс')

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())