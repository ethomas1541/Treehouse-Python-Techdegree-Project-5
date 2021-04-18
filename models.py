import datetime

from peewee import *

db = SqliteDatabase('entries.db')


class Entry(Model):
    """
    The database model for handling all records. The ID is defined
    automatically and forms the basis for viewing, editing or deleting a given
    record.
    """
    ID = PrimaryKeyField()
    title = TextField()
    date = DateField(default=datetime.date.today)
    time = IntegerField()
    learned = TextField()
    resources = TextField()

    class Meta:
        database = db

# Only create tables if this file is running as a module

if __name__ == "models":
    db.create_tables([Entry], safe=True)
