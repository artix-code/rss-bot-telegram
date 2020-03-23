# RSS-feed bot from Telegram
# Author: Artik Zenevich 2020

import telebot
# внешние файлы
import config
import feed

bot = telebot.TeleBot(config.TOKEN)

# стартовая команда приветствия
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Ghbdtn")

# получение новостей
@bot.message_handler(commands=['news'])
def news(message):
    
    # внешняя функция из файла feed.py
    all_links = feed.get_news(config.NEWS_URL) # функция возвращает массив ссылок 
    for n in all_links:
        bot.send_message(message.chat.id, n)

# вывод сообщения если пользователь отправил просто текст, а не команду
@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(message.chat.id, "Пожалуйста введите команду, я болтать с Вами не собираюсь...")

bot.polling(none_stop=True)