from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CallbackContext
from db import DB

db = DB('db.json')

class Auth_bot:
    def start(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(
            'Assalomu alaykum, Iltimos, ismingizni kiriting'
        )
        reply_markup = ReplyKeyboardMarkup(
            [["ro'yxatdan o'tish"]], resize_keyboard=True, one_time_keyboard=True
        )
        update.message.reply_text(
            "Ro'yxatdan o'tish uchun quydagi buttoni bosing",
            reply_markup=reply_markup
        )
    
    def direction_user(self, update: Update, context: CallbackContext):
        username = update.message.from_user.username
        if username:
            bot = context.bot
            chat_id = update.message.chat_id
            text = "Quydagi namuna asosida malumotni\nto'ldiring va botga yuboring\n\n"
            text += "ism:___\nfamiliya:___\nsharif:___\ntelefon:___\nyo'nalish:___\ngmail:___\n"
            bot.send_message(chat_id=chat_id, text=text)

        else:
            update.message.reply_text(
                'Iltimos, telegramdagi ismingizni\n shaxsiy kabinetga kiriting va /start \nbuyrug\'ini qayta bering'
            )