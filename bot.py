import telebot
from telebot import types

bot = telebot.TeleBot('7053088731:AAFgdmKAZ643ZuyYddEIOOGB5ckt9TdEEMU')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Каталог")
    markup.add(btn1)
    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Каталог':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Стим')
        btn2 = types.KeyboardButton('Стим услуги')
        btn3 = types.KeyboardButton('тг прем')
        btn4 = types.KeyboardButton('discord nitro')
       
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, 'че тебе надо', reply_markup=markup) #ответ бота


    elif message.text == 'Стим':
        bot.send_message(message.from_user.id, 'Ле куда преш', parse_mode= 'Markdown')
    elif message.text == 'Стим услуги':
        bot.send_message(message.from_user.id, 'сдачу не дам', parse_mode='Markdown')
    elif message.text == 'тг прем':
        bot.send_message(message.from_user.id, 'чистка труб звонить 890342342233', parse_mode='Markdown')
    elif message.text == 'discord nitro':
        bot.send_message(message.from_user.id, 'ты даун?', parse_mode='Markdown')
    


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть