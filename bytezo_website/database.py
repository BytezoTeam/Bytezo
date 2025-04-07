from peewee import SqliteDatabase, TextField, Model
from uuid import uuid4

db = SqliteDatabase("database/database.db")


class Messages(Model):
    id = TextField(primary_key=True)
    name = TextField()
    email = TextField()
    message = TextField()

    class Meta:
        database = db


class Database:
    def __init__(self: "Database") -> None:
        self.db = db
        self.db.connect()
        self.db.create_tables([Messages])


def add_message(email: str, message: str, name: str) -> Messages:
    return Messages.create(id=str(uuid4()), name=name, email=email, message=message)


def get_message(message_id: str) -> Messages:
    return Messages.get(Messages.id == message_id)


def delete_message(message_id: str) -> None:
    Messages.get(Messages.id == message_id).delete_instance()
