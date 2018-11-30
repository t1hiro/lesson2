import logging
from datetime import datetime

import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from settings import API_KEY, PROXY

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def get_planet(bot, update):
    text = update.message.text.split()
    logging.info(text)
    try:
        if len(text) == 1:
            update.message.reply_text('Введите значение после команды /planet')
        planet = getattr(ephem, text[1])(datetime.now().strftime('%Y/%m/%d/'))
        _, constellation_name = ephem.constellation(planet)
        update.message.reply_text(constellation_name)
    except AttributeError:
        update.message.reply_text('Такой планеты не существует')


def talk_to_me(bot, update):
    user_text = "Привет, {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username, 
    	update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    logging.info('Бот запускается')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()