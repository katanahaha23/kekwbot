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

#снизу чисто инфа

    elif message.text == 'ТГ Канал':
        bot.send_message(message.from_user.id, "тут ссылка на канал")
    elif message.text == 'Контакты':
        bot.send_message(message.from_user.id, '@ccody')
    

#отдельно кнопки для каждой услуги



@bot.message_handler(commands=['start'])
def get_back(message):
    if message.text == 'НАЗАД': 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Каталог')
        btn2 = types.KeyboardButton('ТГ Канал')
        btn3 = types.KeyboardButton('Контакты')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Общая информация o боте будет в этом сообщении", reply_markup=markup)



@bot.message_handler(content_types=['text'])
def get_usluges(message):

    if message.text == 'Steam товары':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Выберите товар из списка:",reply_markup=markup)

    elif message.text == 'Steam услуги':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Выберите услугу из списка:",reply_markup=markup)
    elif message.text == 'Telegram Premium':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Ждите, наш администратор скоро пришлет реквизиты для пополнения. Не забудьте прикрепить квитанцию об оплате",reply_markup=markup)
    elif message.text == 'Discord Nitro':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "ты даун",reply_markup=markup)
    
    




    
        
    
        




bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть