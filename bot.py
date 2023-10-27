from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from db import DB
import re

db = DB('db.json')

class Auth_bot:
    def __init__(self) -> None:
        pass

    def start(self, update: Update, context: CallbackContext) -> None:
        bot = context.bot
        if update.message.from_user.username == 'oquvvatullayev':
            update.message.reply_text(
            'Assalomu alaykum✋'
           )
            reply_markup = ReplyKeyboardMarkup(
            [['users info']], resize_keyboard=True, one_time_keyboard=True
             )
            update.message.reply_text(
            "Assalomu alaykum, bizning botimizga hush kelibsiz\n\nBiz siz bilan bog'lanishga doimo tayyormiz ❕",
            reply_markup=reply_markup
            )
        
        else:
            reply_markup = ReplyKeyboardMarkup(
                [['kontakt'],["ro'yxatdan o'tish"]], resize_keyboard=True, one_time_keyboard=True
            )
            update.message.reply_text(
                "Biz siz bilan bog'lanishga doimo tayyormiz ❕",
                reply_markup=reply_markup
            )

    def get_fil(self, update: Update, context: CallbackContext):
        bot = context.bot
        users_file = open("users.csv", "rb")
        chat_id = update.message.chat_id
        
        bot.sendMessage(chat_id, text = 'Iltimos kuting ...')
        
        context.bot.send_document(chat_id, users_file)

    def get_contact(self, update: Update, context: CallbackContext):
        chat_id = update.message.chat_id
        bot = context.bot
        con = db.get_contakt()
        
        name = con['name']
        suername = con['surname']
        phone1 = con['phone1']
        phone2 = con['phone2']
        tg = con['username']
        instagram = con['instagram']

        text = f"Admin ismi : {suername} {name}\n\nTel1 : {phone1} \n Tel2 : {phone2}\n\nTelegram : {tg}\n\nInstagram : {instagram}"

        bot.sendMessage(text = text, chat_id = chat_id)
        
    def direction_user(self, update: Update, context: CallbackContext):
        username = update.message.from_user.username
        if username:
            bot = context.bot
            chat_id = update.message.chat_id
            text = "Quydagi namuna asosida malumotni\nto'ldiring va botga yuboring📝\n\n"
            text += "ism:Muhammad\n"
            bot.send_message(chat_id=chat_id, text=text)

        else:
            update.message.reply_text(
                'Iltimos, telegramdagi ismingizni\n shaxsiy kabinetga kiriting va /start \nbuyrug\'ini qayta bering ‼️'
            )

    def auth_user(self, update: Update, context: CallbackContext):
        text = update.message.text
        telegram = update.message.from_user.username
        chat_id = update.message.chat_id
        try:
            if telegram:
                get_append = db.get_user_append(chat_id)
                if text == "ro'yxatdan o'tish":
                    if db.chack_user(chat_id) == "200":
                        update.message.reply_text(
                            'Siz ro\'yxatdan o\'tgansiz ‼️'
                        )
                    elif db.chack_user(chat_id) == "401":
                        db.user_append(chat_id)
                        update.message.reply_text(
                            'Iltimos, ismingizni 📝\n\nNamuna: Muhammad'
                        )
            
                elif get_append.get("name") == None:
                    db.user_append(chat_id, name=text, telegram=telegram)
                    update.message.reply_text(
                        'Familiyangizni kiriting📝\n\nNamuna: Abdullayev'
                    )
                elif get_append.get("surname") == None:
                    db.user_append(chat_id, surname=text)
                    update.message.reply_text(
                        'Telefon raqamingizni kiriting📲\n\nNamuna: +998 99 999 99 99'
                    )
                elif get_append.get("phone") == None:
                        pattern = r'\+998\s?\d{2}\s?\d{3}\s?\d{2}\s?\d{2}'
                        telefonlar = re.findall(pattern, text)
                        if telefonlar:
                            db.user_append(chat_id, phone=text)
                            update.message.reply_text(
                                'Yashash manzilingizni kiriting(shahar yoki tuman)📍\n\nNamuna: Toshkent shahar'
                            )
                        else:
                            update.message.reply_text(
                                'Telefon raqamingizni noto\'g\'ri kiritdingiz❌\n\nNamuna: +998 99 999 99 99'
                            )
                elif get_append.get("area") == None:
                    db.user_append(chat_id, area=text)

                    get_append_user = db.get_user_append(chat_id)

                    name = get_append_user.get("name")
                    surname = get_append_user.get("surname")
                    phone = get_append_user.get("phone")
                    area = get_append_user.get("area")
                    inline_keyboard = [
                        [
                            InlineKeyboardButton(
                                text="Yes", callback_data=f"yes_{telegram}"
                            ),
                            InlineKeyboardButton(
                                text="No", callback_data="no"
                            )
                        ]
                    ]

                    reply_markup = InlineKeyboardMarkup(inline_keyboard)


                    update.message.reply_text(
                        f'Ma\'lumotlaringizni tekshirib yuboring✅\n\nIsm: {name}\nFamiliya: {surname}\nTelefon raqam: {phone}\nYashash manzil: {area}\n\nAgar ma\'lumotlar to\'g\'ri bo\'lsa yes, to\'g\'ri emas bo\'lsa no ni bosing👇',
                        reply_markup=reply_markup
                    )
            else:
                update.message.reply_text(
                    'Iltimos, telegramdagi ismingizni\n shaxsiy kabinetga kiriting va /start \nbuyrug\'ini qayta bering ‼️'
                )
        except:
            pass

    def yes(self, update: Update, context: CallbackContext):
        query = update.callback_query
        chat_id = query.message.chat_id
        data = query.data
        telegram = data.split('_')[-1]
        
        get_user_append = db.get_user_append(chat_id)
        name = get_user_append.get("name")
        surname = get_user_append.get("surname")
        phone = get_user_append.get("phone")
        area = get_user_append.get("area")
        query.message.edit_text(
            f'Ma\'lumotlaringiz bazaga saqlanmoqda⏳',
            reply_markup=None
        )
        db.add_user(chat_id, name, surname, phone, telegram, area)
        query.message.reply_text(
            'Sizning ma\'lumotlaringiz bazaga saqlandi✅'
        )
        db.delete_user_append(chat_id)

    def no(self, update: Update, context: CallbackContext):
        query = update.callback_query
        chat_id = query.message.chat_id
        query.message.edit_text(
            'Ma\'lumotlaringizni qayta to\'ldiring📝',
            reply_markup=None
        )
        db.delete_user_append(chat_id)
        query.message.reply_text(
            'Iltimos, ro\'yxatdan o\'tish uchun\n pasdagi tugmani bosing👇'
        )