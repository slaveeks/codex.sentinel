from pymongo import MongoClient
import random
import string

client = MongoClient('127.0.0.1', 27017)
db = client.sentinel

class Duties:
    def __init__(self, username, date):
        self.username = username
        self.date = date

    @staticmethod
    def get_token(chat_id):
        attendant = db.attendants.find_one({'chat_id': chat_id})
        token = attendant['token']
        return token


    @staticmethod
    def generate_token(username, chat_id):
        token = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
        db.attendants.insert_one({'username': username, 'chat_id': chat_id, 'token': token})

    @staticmethod
    def check_token(token):
        answer = db.attendants.find_one({'token': token})
        if answer == None:
            return False
        return True

    def check_user(self):
        answer = db.attendants.find_one({'username': self.username})
        if answer == None:
            return False
        return True

    def new_duty(self):
        if self.check_user():
            db.duties.insert_one({'username': self.username, 'date': self.date})

    @staticmethod
    def find_duty(date):

        data = db.duties.find_one({'date': date})
        if data == None:
            return None
        else:
            attendant = db.attendants.find_one({'username': data['username']})
            return attendant['chat_id']

    @staticmethod
    def check_chat_id(chat_id):
        attendant = db.attendants.find_one({'chat_id': chat_id})
        if attendant == None:
            return False
        return True
