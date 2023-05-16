from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CallbackContext
from db import DB

db = DB('db.json')

class Auth_bot:
    def start(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(
            'Assalomu alaykum, Iltimos, ismingizni kiriting'
        )
        return 'name'