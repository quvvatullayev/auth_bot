from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from bot import Auth_bot

TOKEN = '6750740936:AAHiPpAnBfWYYZZTyy9SGZLVAXybSxYmVKM'

app = Flask(__name__)

bot = Bot(TOKEN)
auth_bot = Auth_bot()


@app.route('/', methods=['POST'])
def index():
    dispatcher = Dispatcher(bot, None, workers=0)

    data = request.get_json(force=True)
    update = Update.de_json(data, bot)

    dispatcher.add_handler(CommandHandler('start', bot.start))
    dispatcher.add_handler(MessageHandler(Filters.text('kontakt'), bot.get_contact))
    dispatcher.add_handler(MessageHandler(Filters.text, bot.auth_user))
    dispatcher.add_handler(CallbackQueryHandler(bot.yes, pattern='yes'))
    dispatcher.add_handler(CallbackQueryHandler(bot.no, pattern='no'))


    dispatcher.process_update(update)
    return 'ok'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.set_webhook('https://authbot.pythonanywhere.com/')
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
    

@app.route('/deletewebhook', methods=['GET', 'POST'])
def delete_webhook():
    s = bot.delete_webhook()
    if s:
        return "webhook delete ok"
    else:
        return "webhook delete failed"