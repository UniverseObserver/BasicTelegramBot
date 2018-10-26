import requests
from telegram.ext import Updater, MessageHandler, Filters
from decouple import config

token = config('TOKEN')
updater = Updater(token=token)
dispatcher = updater.dispatcher

def stalk(bot, update):
    incoming = update.message.text
    #ret = 'I do not understand what you are talking about. '
    ret = '咕咕咕 '
    if (incoming.lower() == 'hello') or (incoming.lower() == 'hi'):
        ret = 'Hi. I am Harry.'
    update.message.reply_text(ret)

dispatcher.add_handler(MessageHandler(Filters.text, stalk))

updater.start_polling()
updater.idle()
