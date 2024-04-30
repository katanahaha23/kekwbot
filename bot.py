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


@dp.message_handler(commands=['start'])
async def alarm(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    user_id_btn = types.InlineKeyboardButton('Получить ID пользывателя из Inline кнопки', callback_data= 'user_id')
    keyboard_markup.row(user_id_btn)
    await message.answer(f"Ваш ID: {message.from_user.id}", reply_markup=keyboard_markup)
 
@dp.callback_query_handler(text='user_id')
async def user_id_inline_callback(callback_query: types.CallbackQuery):
    await callback_query.answer(f"Ваш ID: {callback_query.from_user.id}", True)


    
    
    

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