import telebot
import sqlite3 as sql
#База Данных
con = sql.connect("data.db", check_same_thread=False)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(id INT)")

from telebot import types

bot = telebot.TeleBot('7053088731:AAFgdmKAZ643ZuyYddEIOOGB5ckt9TdEEMU')

#ID Вашего канала
chan_id = -1002072999477

#Клавиатура для проверки подписки
keyboard = telebot.types.InlineKeyboardMarkup()
subscribe = telebot.types.InlineKeyboardButton(text="Подписаться", url="https://t.me/farmcs2news")
check = telebot.types.InlineKeyboardButton(text="Проверить", callback_data="check")
keyboard.add(subscribe)
keyboard.add(check)




@bot.message_handler(commands=['start'])
def start(message):
    users = cur.execute("SELECT id FROM users WHERE id = ?", (message.chat.id, )).fetchone()
    con.commit()
    if users == None:
        bot.send_message(message.from_user.id, "Вы не подписались на канал")
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Каталог')
        btn2 = types.KeyboardButton('ТГ Канал')
        btn3 = types.KeyboardButton('Контакты')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Общая информация o боте будет в этом сообщении", reply_markup=markup)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Каталог':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('Товары')
        btn2 = types.KeyboardButton('Услуги')
        btn3 = types.KeyboardButton('Telegram Premium')
        btn4 = types.KeyboardButton('Discord Nitro')
        btn5 = types.KeyboardButton('НАЗАД')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, 'че тебе надо выбирай', reply_markup=markup) 
    elif message.text == 'ТГ Канал':
        bot.send_message(message.from_user.id, "тут ссылка на канал")
    elif message.text == 'Контакты':
        bot.send_message(message.from_user.id, '@ccody')

    elif message.text == 'Товары':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Выберите товар из списка:', reply_markup=markup)
    elif message.text == 'Услуги':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Выберите услугу из списка:",reply_markup=markup)
    elif message.text == 'Telegram Premium':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Ждите, наш администратор скоро пришлет реквизиты для пополнения. He забудьте прикрепить квитанцию o оплате",reply_markup=markup)
    elif message.text == 'Discord Nitro':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "ты даун",reply_markup=markup)
    
    elif message.text == 'Вернуться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('Товары')
        btn2 = types.KeyboardButton('Услуги')
        btn3 = types.KeyboardButton('Telegram Premium')
        btn4 = types.KeyboardButton('Discord Nitro')
        btn5 = types.KeyboardButton('НАЗАД')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, 'че тебе надо выбирай', reply_markup=markup) 
    
    elif message.text == 'НАЗАД':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Каталог')
        btn2 = types.KeyboardButton('ТГ Канал')
        btn3 = types.KeyboardButton('Контакты')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Общая информация o боте будет в этом сообщении", reply_markup=markup)





bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть