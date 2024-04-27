import telebot
from telebot import types

bot = telebot.TeleBot('7053088731:AAFgdmKAZ643ZuyYddEIOOGB5ckt9TdEEMU')

@bot.message_handler(commands=['start'])
def menu(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Каталог')
    btn2 = types.KeyboardButton('ТГ Канал')
    btn3 = types.KeyboardButton('Контакты')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, "Общая информация o боте будет в этом сообщении", reply_markup=markup)


