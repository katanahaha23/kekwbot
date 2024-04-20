import telebot
from telebot import types

bot = telebot.TeleBot('7053088731:AAFgdmKAZ643ZuyYddEIOOGB5ckt9TdEEMU')

@bot.message_handler(commands=['start'])
def start(message):
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
        btn1 = types.KeyboardButton('Steam товары')
        btn2 = types.KeyboardButton('Steam услуги')
        btn3 = types.KeyboardButton('Telegram Premium')
        btn4 = types.KeyboardButton('Discord Nitro')
        btn5 = types.KeyboardButton('НАЗАД')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, 'че тебе надо выбирай', reply_markup=markup) 
        if message.text == 'Steam товары':
            bot.send_message(message.from_user.id, "ты даун")
    elif message.text == 'ТГ Канал':
        bot.send_message(message.from_user.id, "тут ссылка на канал")
    elif message.text == 'Контакты':
        bot.send_message(message.from_user.id, '@ccody')



bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть