from peewee import *
from uuid import uuid4

db = SqliteDatabase("database.db")

class Messages(Model):
    id = TextField(primary_key=True)
    name = TextField()
    email = TextField()
    message = TextField()

    class Meta:
        database = db


class database():
    def __init__(self):
        self.db = db
        self.db.connect()
        self.db.create_tables([Messages])
    
    def add_message(self, email: str, message: str, name: str):
        return Messages.create(
            id = str(uuid4()),
            name = name,
            email = email,
            message = message
        )
    
    def delete_message(self, id):
        Messages.get(Messages.id == id).delete_instance()
        return True