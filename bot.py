import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder


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
        [
            types.KeyboardButton(text="Каталог"),
            types.KeyboardButton(text="Тг Канал"),
            types.KeyboardButton(text="Отзывы")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите..."
    )
    await message.answer("Добро пожаловать в СЫС ЭНТЕРТЕЙМЕНТ бота", reply_markup=keyboard)

# Ответ на команду Каталог, Тг канал и Отзывы
@dp.message(F.text.lower() == "Каталог")
async def cataloge(message: types.Message):
    await message.answer("Выберите категорию:")

@dp.message(F.text.lower() == "Тг Канал")
async def cataloge(message: types.Message):
    await message.answer("Выберите категорию:")

@dp.message(F.text.lower() == "Отзывы")
async def cataloge(message: types.Message):
    await message.answer("Выберите категорию:")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())