from tinydb import TinyDB
from tinydb.table import Document

class DB:
    def __init__(self, path) -> None:
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.users = self.db.table('users')
        self.data_append = self.db.table('user_data')

    def add_user(self, chat_id, name, surname, phone, telegram, area, school, class_):
        if not self.users.get(doc_id=int(chat_id)):

            self.users.insert(Document({
                "chat_id": chat_id,
                "name": name,
                "surname": surname,
                "phone": phone,
                "username": telegram,
                "area": area,
                "school": school,
                "class": class_
                }, doc_id=chat_id))
            return 'OK 200'
        else:
            return "NO 401"

    def get_user(self, chat_id):
        chat_id = int(chat_id)
        return self.users.get(doc_id=chat_id)
    
    def chack_user(self, chat_id):
        chat_id = int(chat_id)
        if self.users.get(doc_id=chat_id):
            return "200"
        else:
            return "401"
        
    def user_append(self, chat_id, name=None, surname=None, phone=None, telegram=None, area=None, school=None, class_=None):
        chat_id = int(chat_id)
        if not self.data_append.get(doc_id=chat_id):
            self.data_append.insert(Document({
                "chat_id": chat_id,
                "name": None,
                "surname": None,
                "phone": None,
                "username": None,
                "area": None,
                "school": None,
                "class": None
                }, doc_id=chat_id))
        else:
            if name:
                self.data_append.update({"name": name}, doc_ids=[chat_id])
            if surname:
                self.data_append.update({"surname": surname}, doc_ids=[chat_id])
            if phone:
                self.data_append.update({"phone": phone}, doc_ids=[chat_id])
            if telegram:
                self.data_append.update({"username": telegram}, doc_ids=[chat_id])
            if area:
                self.data_append.update({"area": area}, doc_ids=[chat_id])
            if school:
                self.data_append.update({"school": school}, doc_ids=[chat_id])
            if class_:
                self.data_append.update({"class": class_}, doc_ids=[chat_id])
            return self.data_append.get(doc_id=chat_id)
    
    def get_user_append(self, chat_id):
        chat_id = int(chat_id)
        return self.data_append.get(doc_id=chat_id)

    def delete_user_append(self, chat_id):
        chat_id = int(chat_id)
        self.data_append.remove(doc_ids=[chat_id])
        
