import asyncio
from random import choice
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.methods.delete_message import DeleteMessage
import keyboards

bot = Bot("7053088731:AAFgdmKAZ643ZuyYddEIOOGB5ckt9TdEEMU")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Здарова {message.from_user.first_name}", reply_markup=keyboards.main_kb)
    await bot.delete_message(message.chat.id, message.message_id)
    


@dp.message()
async def echo(message: Message):
    msg = message.text.lower()




    if msg == "steam товары":
        await message.answer(f"Выберите интересующий вас товар: ", reply_markup=keyboards.steam_tovary_kb)
        await bot.delete_message(message.chat.id, message.message_id)
        


    elif msg == "steam gifts [5$]":
        await message.answer(f"Перейдите по ссылке и напишите продавцу:", reply_markup=keyboards.gifts_kb)
        await bot.delete_message(message.chat.id, message.message_id)

    elif msg == "аккаунты cs2 prime [13.5$ - 13.9$]":
        await message.answer(f"Выберите товар:", reply_markup=keyboards.accsprime_kb)
        await bot.delete_message(message.chat.id, message.message_id)

    elif msg == "пустышки":
        await message.answer(f"Выберите товар:", reply_markup=keyboards.pustyshki_kb)
        await bot.delete_message(message.chat.id, message.message_id)




    elif msg == "2 ранг, mafiles":
        await message.answer(f"Вам отправлена ссылка на товар: ", reply_markup=keyboards.gifts_kb)
        await bot.delete_message(message.chat.id, message.message_id)

    elif msg == "1 ранг, mafiles":
        await message.answer(f"Вам отправлена ссылка на товар: ", reply_markup=keyboards.gifts_kb)
        await bot.delete_message(message.chat.id, message.message_id)

    elif msg == "пустышки prime cs2, mafiles":
        await message.answer(f"Вам отправлена ссылка на товар: ", reply_markup=keyboards.gifts_kb)
        await bot.delete_message(message.chat.id, message.message_id)

    elif msg == "2 ранг prime cs2, mafiles":
        await message.answer(f"Вам отправлена ссылка на товар: ", reply_markup=keyboards.gifts_kb)
        await bot.delete_message(message.chat.id, message.message_id)





    elif msg == "назад":
        await message.answer(f"Выберите интересующую вас категорию: ", reply_markup=keyboards.cataloge_kb)
        await bot.delete_message(message.chat.id, message.message_id)
    
    elif msg == "вернуться":
        await message.answer(f"Выберите интересующий вас товар: ", reply_markup=keyboards.steam_tovary_kb)
        await bot.delete_message(message.chat.id, message.message_id)
    






    elif msg == "каталог":
        await message.answer(f"Выберите интересующую вас категорию: ", reply_markup=keyboards.cataloge_kb)
        await bot.delete_message(message.chat.id, message.message_id)
    elif msg == "отзывы":
        await message.answer(f"Отзыв вы можете написать нажав на кнопку под сообщением", reply_markup=keyboards.otzyv_kb)
        await bot.delete_message(message.chat.id, message.message_id)
    elif msg == "контакты":
        await message.answer(f"Чтобы связаться с Админом канала нажмите на кнопку ниже", reply_markup=keyboards.contacts_kb)
        await bot.delete_message(message.chat.id, message.message_id)
    





    else:
        answers = [
            "че ты высрал? Чтобы начать напиши /start",
            "завали ебало и нажми /start",
            "чувак иди нахуй. /start",
            "ну давай высри еще. /start для начала.",
            "может напишешь уже /start ?"
        ]
        await bot.delete_message(message.chat.id, message.message_id)
        await message.reply(choice(answers))




async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())