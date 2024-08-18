from peewee import *

db = SqliteDatabase("emailsenha.db")

class emailsenha(Model):
    nome = CharField(unique=True)
    email = CharField(unique=True)
    senha = CharField()

    class Meta:
        database = db
