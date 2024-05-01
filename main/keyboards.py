from aiogram.types import(
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup

)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Каталог"),
            KeyboardButton(text="Контакты"),
            KeyboardButton(text="Отзывы")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите одну чушь из спискa:"
)

cataloge_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Steam Товары"),
            KeyboardButton(text="Steam Услуги"),
            KeyboardButton(text="Telegram Premium")
        ],
        [
            KeyboardButton(text="Discord Nitro"),
            KeyboardButton(text="Главное меню")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите одну чушь из спискa:"
)

otzyv_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="ОТЗЫВЫ", url="https://www.youtube.com/@ex4mpl3")
        ]
    ]
)

contacts_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="КОНТАКТЫ", url="https://t.me/Ccody")
        ]
    ]
)

steam_tovary_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Steam Gifts [5$]"),
            KeyboardButton(text="Аккаунты CS2 Prime [13.5$ - 13.9$]")
        ],
        [
            KeyboardButton(text="Пустышки"),
            KeyboardButton(text="НАЗАД")       
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите товар:"
)

gifts_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ссылка на продавца...", url="https://select-place.ru/product/1734")
        ]
    ]
)




pustyshki_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="2 Ранг, maFiles"),
            KeyboardButton(text="1 Ранг, maFiles")
        ],
        [
            KeyboardButton(text="Вернуться")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите товар:"
)

steam_uslugi_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Прокачка"),
            KeyboardButton(text="Фарм CS2"),
            KeyboardButton(text="Мгновенное пополнение Steam")
        ],
        [
            KeyboardButton(text="Фермер с нуля"),
            KeyboardButton(text="НАЗАД")       
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите товар:"
)
