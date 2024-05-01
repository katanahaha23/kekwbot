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
    await message.answer(f"Приветствуем тебя, {message.from_user.first_name}, в нашем боте - Бутик Гифтов", reply_markup=keyboards.main_kb)
    
    


@dp.message()
async def echo(message: Message):
    msg = message.text.lower()



# выдает стим товары
    if msg == "steam товары":
        await message.answer(f"Выберите интересующий вас товар:",reply_markup=keyboards.steam_tovary_kb)


# выдает стим услуги
    elif msg == "steam услуги":
        await message.answer(f"Выберите интересующую вас услугу:", reply_markup=keyboards.steam_uslugi_kb)

# выдает телеграмм премиум
    elif msg == "telegram premium":
        await message.answer(f"Перейдите по ссылке и напишите продавцу:")
        await message.answer("💳 ВАРИАНТЫ ОПЛАТЫ 💳\nЛюбые карты — Visa | МИР | MasterCard\nКрипта — USDT | TRX | BTC | ETH \nLZT 🐊 — к цене +8%\nКлючи TF2🔑 — по цене уточнять у продавца", reply_markup=keyboards.gifts_kb)


# выдает дискорд нитро
    elif msg == "discord nitro":
        await message.answer(f"Перейдите по ссылке и напишите продавцу:")
        await message.answer("💳 ВАРИАНТЫ ОПЛАТЫ 💳\nЛюбые карты — Visa | МИР | MasterCard\nКрипта — USDT | TRX | BTC | ETH \nLZT 🐊 — к цене +8%\nКлючи TF2🔑 — по цене уточнять у продавца", reply_markup=keyboards.gifts_kb)





        

# стим товары
    elif msg == "steam gifts [5$]":
        await message.answer(f"📌 Price Gift Card 👀\n👾 40HKD — 5.1 $ дает на баланс (Подходит для 🇺🇦,🇰🇿 и остальных СНГ стран кроме 🇷🇺)\n💵 Цена — 5.00 $")
        await message.answer("💳 ВАРИАНТЫ ОПЛАТЫ 💳\nЛюбые карты — Visa | МИР | MasterCard\nКрипта — USDT | TRX | BTC | ETH \nLZT 🐊 — к цене +8%\nКлючи TF2🔑 — по цене уточнять у продавца", reply_markup=keyboards.gifts_kb)
# прайм кс
    elif msg == "аккаунты cs2 prime [13.75$ - 14.25$]":
        await message.answer(f"📌 Аккаунты Prime CS2, maFiles \n💵 Пустышка, Prime CS2 — 13.75 $\n💵 2 ранг, Prime CS2 — 14.25 $")
        await message.answer("💳 ВАРИАНТЫ ОПЛАТЫ 💳\nЛюбые карты — Visa | МИР | MasterCard\nКрипта — USDT | TRX | BTC | ETH \nLZT 🐊 — к цене +8%\nКлючи TF2🔑 — по цене уточнять у продавца", reply_markup=keyboards.gifts_kb)
# пустышки
    elif msg == "пустышки":
        await message.answer(f"Выберите товар:", reply_markup=keyboards.pustyshki_kb)
        




        
# пустышки
    elif msg == "1 ранг, mafiles":
        await message.answer(f"📌 Аккаунты пустышки, 1 ранг, maFiles\n💵 50шт — 12.50 $\n💵 100шт — 25.00 $")
        await message.answer("💳 ВАРИАНТЫ ОПЛАТЫ 💳\nЛюбые карты — Visa | МИР | MasterCard\nКрипта — USDT | TRX | BTC | ETH \nLZT 🐊 — к цене +8%\nКлючи TF2🔑 — по цене уточнять у продавца", reply_markup=keyboards.gifts_kb)


    elif msg == "2 ранг, mafiles":
        await message.answer(f"📌 Готовые аккаунты пустышки, имеется 2 ранг, maFiles \n1. Полученный руками, прокачка по 1 аккаунту за раз\n💵 10-50 шт — 1.1$\шт\n💵 50-∞ шт — 1$\шт\n\n2. Полученный захватом сервера, прокачка по 12 аккаунтов за раз\n💵 10-50 шт — 0.8$\шт\n💵 50-∞ шт — 0.75$\шт")
        await message.answer("💳 ВАРИАНТЫ ОПЛАТЫ 💳\nЛюбые карты — Visa | МИР | MasterCard\nКрипта — USDT | TRX | BTC | ETH \nLZT 🐊 — к цене +8%\nКлючи TF2🔑 — по цене уточнять у продавца", reply_markup=keyboards.gifts_kb)


# прокачка
    elif msg == "прокачка 2-го ранга":
        await message.answer(f"📌 Прокачка 2-го приватного ранга\n1. Полученный руками, прокачка по 1 аккаунту за раз\n💵 10-50 шт —  0,8$\шт\n💵 50-∞ шт — 0,7$\шт\n\n2. Полученный захватом сервера, прокачка по 12 аккаунтов за раз\n💵 10-50 шт —  0.6$\шт\n💵 50-∞ шт — 0.5$\шт")
        await message.answer("💳 ВАРИАНТЫ ОПЛАТЫ 💳\nЛюбые карты — Visa | МИР | MasterCard\nКрипта — USDT | TRX | BTC | ETH \nLZT 🐊 — к цене +8%\nКлючи TF2🔑 — по цене уточнять у продавца", reply_markup=keyboards.gifts_kb)


# фарм кс 
    elif msg == "фарм cs2":
        await message.answer(f"📌 Фарм ваших аккаунтов панелью на ваыбор (Tedon\FSM) 👨‍💻 \n⚡️ 30% — от 10 до 100 аккаунтов\n⚡️ 25% — от 100 до 250 аккаунтов\n⚡️ 20% — от 250 и более")
        await message.answer("💳 ВАРИАНТЫ ОПЛАТЫ 💳\nЛюбые карты — Visa | МИР | MasterCard\nКрипта — USDT | TRX | BTC | ETH \nLZT 🐊 — к цене +8%\nКлючи TF2🔑 — по цене уточнять у продавца", reply_markup=keyboards.gifts_kb)




# фермер с нуля (нахуй)
    elif msg == "фермер с нуля":
        await message.answer(f"📌 Обучающие курсы\n💵 Фермер с нуля — 49.99 $\nВ обучение входят различные гайды, сборки пк и меры предосторожности от VAC")
        await message.answer("💳 ВАРИАНТЫ ОПЛАТЫ 💳\nЛюбые карты — Visa | МИР | MasterCard\nКрипта — USDT | TRX | BTC | ETH \nLZT 🐊 — к цене +8%\nКлючи TF2🔑 — по цене уточнять у продавца", reply_markup=keyboards.gifts_kb)













# кнопки возврата 
    elif msg == "назад":
        await message.answer(f"Выберите интересующую вас категорию: ", reply_markup=keyboards.cataloge_kb)
        
    
    elif msg == "вернуться":
        await message.answer(f"Выберите интересующий вас товар: ", reply_markup=keyboards.steam_tovary_kb)

    
    elif msg == "главное меню":
        await message.answer(f"Доброго вам дня!", reply_markup=keyboards.main_kb)

        
    




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