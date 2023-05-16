from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from db import DB

db = DB('db.json')

class Auth_bot:
    def start(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(
            'Assalomu alaykum, Iltimos, ismingizni kiriting✋'
        )
        reply_markup = ReplyKeyboardMarkup(
            [["ro'yxatdan o'tish"]], resize_keyboard=True, one_time_keyboard=True
        )
        update.message.reply_text(
            "Ro'yxatdan o'tish uchun quydagi buttoni bosing🔐",
            reply_markup=reply_markup
        )
    
    def direction_user(self, update: Update, context: CallbackContext):
        username = update.message.from_user.username
        if username:
            bot = context.bot
            chat_id = update.message.chat_id
            text = "Quydagi namuna asosida malumotni\nto'ldiring va botga yuboring📝\n\n"
            text += "ism:___\nfamiliya:___\nsharif:___\ntelefon:___\nyo'nalish:___\ngmail:___\n"
            bot.send_message(chat_id=chat_id, text=text)

        else:
            update.message.reply_text(
                'Iltimos, telegramdagi ismingizni\n shaxsiy kabinetga kiriting va /start \nbuyrug\'ini qayta bering❕'
            )

    def auth_user(self, update: Update, context: CallbackContext):
        text = update.message.text
        bot = context.bot
        chat_id = update.message.chat_id
        if "ism:" in text and "familiya:" in text and "sharif:" in text and "telefon:" in text and "yo'nalish:" in text and "gmail:" in text:
            text = update.message.text.split('\n')
            telegram_username = update.message.from_user.username
            name = text[0].split(":")[1]
            surname = text[1].split(":")[1]
            fathername = text[2].split(":")[1]
            phone = text[3].split(":")[1]
            direction = text[4].split(":")[1]
            gmail = text[5].split(":")[1]

            if name and surname and fathername and phone and direction and gmail and telegram_username:
                respons = db.add_user(chat_id, name, surname, fathername, phone, telegram_username, direction,gmail)

                if respons == "NO 401":
                    text = "Siz oldinham ro'yxatdan o'tgansiz‼️"
                    bot.sendMessage(chat_id, text)

                elif db.get_user(chat_id) and respons == "OK 200":
                    text = 'Tabriklayman siz movfaqyatli ro\'yxatdan o\'tdingiz✅'
                    bot.sendMessage(chat_id, text)

                else:
                    text = "Ro'yxatdan o'tishda xatolik yuz berdi qayta urinign❌⁉️"
                    bot.sendMessage(chat_id, text)
       
            else:
                text = 'Shablonni hato kritgansiz yoki telegram ismingiz yo\'q⁉️'
                bot.sendMessage(chat_id, text)

        else:
            text = 'Shablonni hato kritgansiz yoki telegram ismingiz yo\'q⁉️'
            bot.sendMessage(chat_id, text)