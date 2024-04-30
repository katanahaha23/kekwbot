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
            KeyboardButton(text="ТГ Канал"),
            KeyboardButton(text="Отзывы")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите одну чушь из спискa:"
)

