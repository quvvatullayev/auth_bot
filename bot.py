from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from db import DB

db = DB('db.json')

class Auth_bot:
    def __init__(self) -> None:
        self.user_data = {}

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
            if text == "ro'yxatdan o'tish":
                if db.chack_user(chat_id) == "200":
                    update.message.reply_text(
                        'Siz ro\'yxatdan o\'tgansiz❕'
                    )
                elif db.chack_user(chat_id) == "401":
                    update.message.reply_text(
                        'Iltimos, ismingizni kiriting✋\n\nNamuna: Muhammad'
                    )
            
            elif self.user_data.get("name") == None:
                self.user_data["name"] = text
                update.message.reply_text(
                    'Familiyangizni kiriting✋\n\nNamuna: Abdullayev'
                )
            elif self.user_data.get("surname") == None:
                self.user_data["surname"] = text
                update.message.reply_text(
                    'Telefon raqamingizni kiriting✋\n\nNamuna: +998901234567'
                )
            elif self.user_data.get("phone") == None:
                self.user_data["phone"] = text
                update.message.reply_text(
                    'Yashash manzilingizni kiriting(shahar yoki tuman)✋\n\nNamuna: Toshkent shahar'
                )
            elif self.user_data.get("area") == None:
                self.user_data["area"] = text
                update.message.reply_text(
                    'Maktabingizni kiriting✋\n\nNamuna: 1-maktab'
                )
            elif self.user_data.get("school") == None:
                self.user_data["school"] = text
                update.message.reply_text(
                    'Sinfingizni kiriting✋\n\nNamuna: 9-sinf'
                )
            elif self.user_data.get("class") == None:
                self.user_data["class"] = text
                name = self.user_data.get("name")
                surname = self.user_data.get("surname")
                phone = self.user_data.get("phone")
                area = self.user_data.get("area")
                school = self.user_data.get("school")
                class_ = self.user_data.get("class")
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

        print(self.user_data)

    def yes(self, update: Update, context: CallbackContext):
        query = update.callback_query
        bot = context.bot
        chat_id = query.message.chat_id
        telegram = query.message.from_user.username
        name = self.user_data.get("name")
        surname = self.user_data.get("surname")
        phone = self.user_data.get("phone")
        area = self.user_data.get("area")
        school = self.user_data.get("school")
        class_ = self.user_data.get("class")
        query.message.edit_text(
            f'Ma\'lumotlaringiz bazaga saqlanmoqda⏳',
            reply_markup=None
        )
        db.add_user(chat_id, name, surname, phone, telegram, area, school, class_)
        query.message.reply_text(
            'Sizning ma\'lumotlaringiz bazaga saqlandi✅'
        )

    def no(self, update: Update, context: CallbackContext):
        query = update.callback_query
        bot = context.bot
        chat_id = query.message.chat_id
        telegram = query.message.from_user.username
        query.message.edit_text(
            'Ma\'lumotlaringizni qayta to\'ldiring✋',
            reply_markup=None
        )
        self.user_data = {}
        query.message.reply_text(
            'Iltimos, ro\'yxatdan o\'tish uchun\n pasdagi tugmani bosing🔐'
        )