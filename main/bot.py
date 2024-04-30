import asyncio
from random import choice

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from aiogram.types import Message

bot = Bot("7053088731:AAFgdmKAZ643ZuyYddEIOOGB5ckt9TdEEMU")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Здарова попуск, {message.from_user.first_name}")
    


@dp.message()
async def echo(message: Message):
    answers = [
        "че ты высрал?",
        "завали ебало",
        "чувак иди нахуй"
    ]
    await message.reply(choice(answers))




async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())