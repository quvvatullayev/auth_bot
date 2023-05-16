from tinydb import TinyDB, Query
from tinydb.table import Document

class DB:
    def __init__(self, path) -> None:
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.users = self.db.table('users')

    def add_user(self, chat_id, name, surname, fathername, phone, telegram, direction, gmail):
        self.users.insert(Document({
            "chat_id": chat_id,
            "name": name,
            "surname": surname,
            "fathername": fathername,
            "phone": phone,
            "telegram": telegram,
            "direction": direction,
            "gmail": gmail
            }, doc_id=chat_id))

    def get_user(self, chat_id):
        chat_id = int(chat_id)
        return self.users.get(doc_id=chat_id)
    
# db = DB('db.json')
# db.add_user('64654', 'Sardor', 'Saidov', 'Saidovich', '+998 99 999 99 99', '@sardor', 'Python', 'quvvatullaye@gmail.com')
# print(db.users.all())
# print(db.get_user(64654))
