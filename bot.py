import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7053088731:AAFgdmKAZ643ZuyYddEIOOGB5ckt9TdEEMU")
# Диспетчер
dp = Dispatcher()

#запуск бота через кнопку

@dp.message(F.text.lower() == True)
async def start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="/start"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer(reply_markup=keyboard)

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

# Ответ на команду Каталог
@dp.message(F.text.lower() == "каталог")
async def cataloge(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Steam услуги"),
            types.KeyboardButton(text="Steam товары"),
            types.KeyboardButton(text="Telegram Premium"),
            types.KeyboardButton(text="Discord Nitro"),
            types.KeyboardButton(text="PornHub +")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите..."
    )
    await message.answer("Выберите категорию:", reply_markup=keyboard)


# Ответ на команду ТГ Канал
@dp.message(F.text.lower() == "тг канал")
async def tg_chan(message: types.Message):
    await message.answer("https://t.me/farmcs2news")


# Ответ на команду Отзывы
@dp.message(F.text.lower() == "отзывы")
async def review(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="ОТЗЫВЫ", url="https://github.com")
    )
    await message.answer('Нажми на ссылку',reply_markup=builder.as_markup(),)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())