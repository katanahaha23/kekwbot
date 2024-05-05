from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from keyboards import channel_kb


class CheckSubscription(BaseMiddleware):

    async def __call__(
        self, 
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], 
        event: Message, 
        data: Dict[str, Any]
    ) -> Any:
        chat_member = await event.bot.get_chat_member("@farmcs2news", event.from_user.id)

        if chat_member.status == "left":
            await event.answer(
                "Для использования бота, подпишитесь на наш канал!",
                reply_markup=channel_kb

            )
        else:
            return await handler(event, data)