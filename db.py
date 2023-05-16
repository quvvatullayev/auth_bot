from tinydb import TinyDB
from tinydb.table import Document

class DB:
    def __init__(self, path) -> None:
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.users = self.db.table('users')

    def add_user(self, chat_id, name, surname, fathername, phone, telegram, direction, gmail):
        if not self.users.get(doc_id=int(chat_id)):
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
            return 'OK 200'
        else:
            return "NO 401"

    def get_user(self, chat_id):
        chat_id = int(chat_id)
        return self.users.get(doc_id=chat_id)