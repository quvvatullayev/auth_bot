from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from bot import Auth_bot

bot = Auth_bot()
TOKEN = '5230794877:AAF7Y5UR88eR4hYSwVuSecoL6SYUFEdDICY'

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', bot.start))


updater.start_polling()
updater.idle()