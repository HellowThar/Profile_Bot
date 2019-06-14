from peewee import *

DATABASE = SqliteDatabase('profiles.sqlite')

class BaseModel(Model):

    class Meta:
        database = DATABASE

class Profile(BaseModel):
    username = CharField(unique=True)
    profile = TextField()

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Profile], safe=True)
    DATABASE.close()
