import asyncio
from distutils.dep_util import newer
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

channelz = ["opp", "-1002072999477", "https://t.me/farmcs2news"]



#проверка подписки на канал
async def check_sub(channels, user_id):
    for channel in channels:
        chat_member = await bot.get_chat_member(chat_id=channel[1],user_id=user_id)
        if chat_member["status"] == "left":
            return False
    return True





# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if await check_sub(channelz, message.from_user.id):
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
    else:
        await bot.send_message(message.from_user.id, "Подписка сначала Ковбой")


# Ответ на команду Каталог
@dp.message(F.text.lower() == "каталог")
async def reply_builder(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Steam услуги")),
    builder.add(types.KeyboardButton(text="Steam товары")),
    builder.add(types.KeyboardButton(text="Telegram Premium")),
    builder.add(types.KeyboardButton(text="Discord Nitro")),
    builder.add(types.KeyboardButton(text="PornHub +")),
    builder.add(types.KeyboardButton(text="Назад"))
    builder.adjust(3)
    await message.answer("Выберите категорию:",reply_markup=builder.as_markup(resize_keyboard=True),)


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

# Ответ на команду Назад
@dp.message(F.text.lower() == "назад")
async def nazad(message: types.Message):
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
    await message.answer("Че хотел?", reply_markup=keyboard)



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())