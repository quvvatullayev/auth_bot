from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from bot import Auth_bot

bot = Auth_bot()
TOKEN = '5230794877:AAF7Y5UR88eR4hYSwVuSecoL6SYUFEdDICY'

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', bot.start))
dispatcher.add_handler(MessageHandler(Filters.text("ro'yxatdan o'tish"), bot.direction_user))
dispatcher.add_handler(MessageHandler(Filters.text, bot.auth_user))


updater.start_polling()
updater.idle()