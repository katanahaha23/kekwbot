import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

bot = Bot("7053088731:AAFgdmKAZ643ZuyYddEIOOGB5ckt9TdEEMU")
dp = Dispatcher()


@dp.message(F.text=="/start")
async def start(message: Message):
    await message.answer(f"Hello, {message.from_user.first_name}")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())