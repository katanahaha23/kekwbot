from aiogram.types import(
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup

)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Каталог"),
            KeyboardButton(text="Контакты"),
            KeyboardButton(text="Отзывы")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
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
            KeyboardButton(text="PornHub Premium")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите одну чушь из спискa:"
)


