from tinydb import TinyDB
from tinydb.table import Document

class DB:
    def __init__(self, path) -> None:
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.users = self.db.table('users')
        self.userdata = self.db.table('user_data')

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
        
    def user_data(self, chat_id, name=None, surname=None, phone=None, telegram=None, area=None, school=None, class_=None):
        chat_id = int(chat_id)
        if self.userdata.get(chat_id = chat_id):
            self.userdata.update(Document({
                "chat_id": chat_id,
                "name": name,
                "surname": surname,
                "phone": phone,
                "username": telegram,
                "area": area,
                "school": school,
                "class": class_
                }, doc_id=chat_id))
        else:
            self.userdata.insert(Document({
                "chat_id": chat_id,
                "name": name,
                "surname": surname,
                "phone": phone,
                "username": telegram,
                "area": area,
                "school": school,
                "class": class_
                }, doc_id=chat_id))
            
    def get_user_data(self, chat_id):
        chat_id = int(chat_id)
        return self.userdata.get(doc_id=chat_id)
        
