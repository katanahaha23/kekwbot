import telebot
from telebot import types

bot = telebot.TeleBot('7053088731:AAFgdmKAZ643ZuyYddEIOOGB5ckt9TdEEMU')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Каталог')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Ты дурак ебаный!", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Каталог':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('пиздапень')
        btn2 = types.KeyboardButton('хуепень')
        btn3 = types.KeyboardButton('залупень')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'ты хуй', reply_markup=markup) 


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть