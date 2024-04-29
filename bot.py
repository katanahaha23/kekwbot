import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7053088731:AAFgdmKAZ643ZuyYddEIOOGB5ckt9TdEEMU")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    
    kb = [
        [types.KeyboardButton(text="Каталог")],
        [types.KeyboardButton(text="ТГ Канал")],
        [types.KeyboardButton(text="Отзывы")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Приветствую тебя в боте СЫС ЭНТЕРТЕЙМЕНТ!", reply_markup=keyboard)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())