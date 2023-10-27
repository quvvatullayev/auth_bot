from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from bot import Auth_bot

bot = Auth_bot()
TOKEN = '5505244566:AAFRwoxaYH-ahK27OKN0_6MPKStev9LJ1R4'

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', bot.start))
dispatcher.add_handler(MessageHandler(Filters.text('kontakt'), bot.get_contact))
dispatcher.add_handler(MessageHandler(Filters.text('users info'), bot.get_fil))
dispatcher.add_handler(MessageHandler(Filters.text('server'), bot.open_url))
dispatcher.add_handler(MessageHandler(Filters.text, bot.auth_user))
dispatcher.add_handler(CallbackQueryHandler(bot.yes, pattern='yes'))
dispatcher.add_handler(CallbackQueryHandler(bot.no, pattern='no'))

                                            
updater.start_polling()
updater.idle()