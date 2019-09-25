import logging
from flask import Flask, request
import os

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater
server = Flask(__name__)

import bot_settings

logging.basicConfig(
    format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

updater = Updater(token=bot_settings.BOT_TOKEN)
dispatcher = updater.dispatcher


def start(bot, update):
    chat_id = update.message.chat_id
    logger.info(f"> Start chat #{chat_id}")
    bot.send_message(chat_id=chat_id, text="💣 Welcome! 💣")


def respond(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")
    response = text.replace("7", "💣")
    bot.send_message(chat_id=update.message.chat_id, text=response)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, respond)
dispatcher.add_handler(echo_handler)

logger.info("Start polling")
updater.start_polling()

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    
