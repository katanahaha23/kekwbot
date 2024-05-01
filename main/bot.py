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
    await bot.delete_message(message.chat.id, message.message_id)
    await message.answer(f"Здарова {message.from_user.first_name}", reply_markup=keyboards.main_kb)
    
    


@dp.message()
async def echo(message: Message):
    msg = message.text.lower()



# выдает стим товары
    if msg == "steam товары":
        await message.answer(f"Выберите интересующий вас товар:", reply_markup=keyboards.steam_tovary_kb)

# выдает стим услуги
    elif msg == "steam услуги":
        await message.answer(f"Выберите интересующую вас услугу:", reply_markup=keyboards.steam_uslugi_kb)

# выдает телеграмм премиум
    elif msg == "telegram premium":
        await message.answer(f"Перейдите по ссылке и напишите продавцу:",reply_markup=keyboards.gifts_kb)

# выдает дискорд нитро
    elif msg == "discord nitro":
        await message.answer(f"Перейдите по ссылке и напишите продавцу:",reply_markup=keyboards.gifts_kb)




        

# стим товары
    elif msg == "steam gifts [5$]":
        await message.answer(f"📌 Price Gift Card 👀\n⚙️ 40HKD — 5.1$ дает на баланс (Подходит для 🇺🇦,🇰🇿 и остальных СНГ стран кроме 🇷🇺)\n💵 Цена — 5.30 $ \n⚙️ 5$ USA — 5$ дает на баланс (Подходит для 🇺🇸 и других ближайших стран)\n💵Цена — 5.30 $ ", reply_markup=keyboards.gifts_kb)
        
# прайм кс
    elif msg == "аккаунты cs2 prime [13.5$ - 13.9$]":
        await message.answer(f"Выберите товар:", reply_markup=keyboards.accsprime_kb)
        
# пустышки
    elif msg == "пустышки":
        await message.answer(f"Выберите товар:", reply_markup=keyboards.pustyshki_kb)
        



# прайм кс
    elif msg == "2 ранг, mafiles":
        
        await message.answer(f"Перейдите по ссылке и напишите продавцу:", reply_markup=keyboards.gifts_kb)
       

    elif msg == "1 ранг, mafiles":
        await message.answer(f"Перейдите по ссылке и напишите продавцу:", reply_markup=keyboards.gifts_kb)
        
# пустышки
    elif msg == "пустышки prime cs2, mafiles":
        await message.answer(f"Перейдите по ссылке и напишите продавцу:", reply_markup=keyboards.gifts_kb)
       

    elif msg == "2 ранг prime cs2, mafiles":
        await message.answer(f"Перейдите по ссылке и напишите продавцу:", reply_markup=keyboards.gifts_kb)
       

# прокачка
    elif msg == "прокачка":
            await message.answer(f"Перейдите по ссылке и напишите продавцу:", reply_markup=keyboards.gifts_kb)

# фарм кс 
    elif msg == "фарм cs2":
        await message.answer(f"Перейдите по ссылке и напишите продавцу:", reply_markup=keyboards.gifts_kb)

# мгновенное пополнение
    elif msg == "мгновенное пополнение steam":
        await message.answer(f"Перейдите по ссылке и напишите продавцу:", reply_markup=keyboards.gifts_kb)

# фермер с нуля (нахуй)
    elif msg == "фермер с нуля":
        await message.answer(f"Перейдите по ссылке и напишите продавцу:", reply_markup=keyboards.gifts_kb)












# кнопки возврата 
    elif msg == "назад":
        await message.answer(f"Выберите интересующую вас категорию: ", reply_markup=keyboards.cataloge_kb)
        
    
    elif msg == "вернуться":
        await message.answer(f"Выберите интересующий вас товар: ", reply_markup=keyboards.steam_tovary_kb)

    
    elif msg == "главное меню":
        await message.answer(f"Приветствуем вас в нашем боте - Бутик Гифтов!", reply_markup=keyboards.main_kb)

        
    




# кнопки основного меню
    elif msg == "каталог":
        await message.answer(f"Выберите интересующую вас категорию: ", reply_markup=keyboards.cataloge_kb)

    elif msg == "отзывы":
        await message.answer(f"Отзыв вы можете написать нажав на кнопку под сообщением", reply_markup=keyboards.otzyv_kb)
        
    elif msg == "контакты":
        await message.answer(f"Чтобы связаться с Админом канала нажмите на кнопку ниже", reply_markup=keyboards.contacts_kb)
        
    




# бот не понимает вашу команду и выдает что то из этого 
    else:
        await bot.delete_message(message.chat.id, message.message_id)
        answers = [
            "че ты высрал? Чтобы начать напиши /start",
            "завали ебало и нажми /start",
            "чувак иди нахуй. /start",
            "ну давай высри еще. /start для начала.",
            "может напишешь уже /start ?"
        ]
        
        await message.answer(choice(answers))




async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())