import asyncio
from distutils.dep_util import newer
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardMarkup
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils.formatting import Text, Bold



sub_channel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подписаться", url="https://t.me/farmcs2news")
        ]
    ]
)
