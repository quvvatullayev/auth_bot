from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from bot import Auth_bot

bot = Auth_bot()
TOKEN = '6750740936:AAHiPpAnBfWYYZZTyy9SGZLVAXybSxYmVKM'

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', bot.start))
dispatcher.add_handler(MessageHandler(Filters.text, bot.auth_user))
dispatcher.add_handler(CallbackQueryHandler(bot.yes, pattern='yes'))
dispatcher.add_handler(CallbackQueryHandler(bot.no, pattern='no'))
                                            
updater.start_polling()
updater.idle()