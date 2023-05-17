from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from db import DB

db = DB('db.json')

class Auth_bot:
    def __init__(self) -> None:
        pass

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
            text += "ism:Muhammad\n"
            bot.send_message(chat_id=chat_id, text=text)

        else:
            update.message.reply_text(
                'Iltimos, telegramdagi ismingizni\n shaxsiy kabinetga kiriting va /start \nbuyrug\'ini qayta bering❕'
            )

    def auth_user(self, update: Update, context: CallbackContext):
        text = update.message.text
        bot = context.bot
        telegram = update.message.from_user.username
        chat_id = update.message.chat_id
        if telegram:
            get_append = db.get_user_append(chat_id)
            if text == "ro'yxatdan o'tish":
                if db.chack_user(chat_id) == "200":
                    update.message.reply_text(
                        'Siz ro\'yxatdan o\'tgansiz❕'
                    )
                elif db.chack_user(chat_id) == "401":
                    db.user_append(chat_id)
                    update.message.reply_text(
                        'Iltimos, ismingizni kiriting✋\n\nNamuna: Muhammad'
                    )
        
            elif get_append.get("name") == None:
                # self.user_data["name"] = text
                db.user_append(chat_id, name=text, telegram=telegram)
                update.message.reply_text(
                    'Familiyangizni kiriting✋\n\nNamuna: Abdullayev'
                )
            elif get_append.get("surname") == None:
                # self.user_data["surname"] = text
                db.user_append(chat_id, surname=text)
                update.message.reply_text(
                    'Telefon raqamingizni kiriting✋\n\nNamuna: +998901234567'
                )
            elif get_append.get("phone") == None:
                # self.user_data["phone"] = text
                db.user_append(chat_id, phone=text)
                update.message.reply_text(
                    'Yashash manzilingizni kiriting(shahar yoki tuman)✋\n\nNamuna: Toshkent shahar'
                )
            elif get_append.get("area") == None:
                # self.user_data["area"] = text
                db.user_append(chat_id, area=text)
                update.message.reply_text(
                    'Maktabingizni kiriting✋\n\nNamuna: 1-maktab'
                )
            elif get_append.get("school") == None:
                # self.user_data["school"] = text
                db.user_append(chat_id, school=text)
                update.message.reply_text(
                    'Sinfingizni kiriting✋\n\nNamuna: 9-sinf'
                )
            elif get_append.get("class") == None:
                # self.user_data["class"] = text
                db.user_append(chat_id, class_=text)
                
                get_append_user = db.get_user_append(chat_id)

                name = get_append_user.get("name")
                surname = get_append_user.get("surname")
                phone = get_append_user.get("phone")
                area = get_append_user.get("area")
                school = get_append_user.get("school")
                class_ = get_append_user.get("class")
                inline_keyboard = [
                    [
                        InlineKeyboardButton(
                            text="Yes", callback_data="yes"
                        ),
                        InlineKeyboardButton(
                            text="No", callback_data="no"
                        )
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(inline_keyboard)


                update.message.reply_text(
                    f'Ma\'lumotlaringizni tekshirib yuboring✋\n\nIsm: {name}\nFamiliya: {surname}\nTelefon raqam: {phone}\nYashash manzil: {area}\nMaktab: {school}\nSinf: {class_}\n\nAgar ma\'lumotlar to\'g\'ri bo\'lsa yes, to\'g\'ri emas bo\'lsa no ni bosing👇',
                    reply_markup=reply_markup
                )
        else:
            update.message.reply_text(
                'Iltimos, telegramdagi ismingizni\n shaxsiy kabinetga kiriting va /start \nbuyrug\'ini qayta bering❕'
            )

        print(get_append)

    def yes(self, update: Update, context: CallbackContext):
        query = update.callback_query
        bot = context.bot
        chat_id = query.message.chat_id
        telegram = query.message.from_user.username
        get_user_append = db.get_user_append(chat_id)
        name = get_user_append.get("name")
        surname = get_user_append.get("surname")
        phone = get_user_append.get("phone")
        area = get_user_append.get("area")
        school = get_user_append.get("school")
        class_ = get_user_append.get("class")
        query.message.edit_text(
            f'Ma\'lumotlaringiz bazaga saqlanmoqda⏳',
            reply_markup=None
        )
        db.add_user(chat_id, name, surname, phone, telegram, area, school, class_)
        query.message.reply_text(
            'Sizning ma\'lumotlaringiz bazaga saqlandi✅'
        )
        db.delete_user_append(chat_id)

    def no(self, update: Update, context: CallbackContext):
        query = update.callback_query
        bot = context.bot
        chat_id = query.message.chat_id
        telegram = query.message.from_user.username
        query.message.edit_text(
            'Ma\'lumotlaringizni qayta to\'ldiring✋',
            reply_markup=None
        )
        db.delete_user_append(chat_id)
        query.message.reply_text(
            'Iltimos, ro\'yxatdan o\'tish uchun\n pasdagi tugmani bosing🔐'
        )