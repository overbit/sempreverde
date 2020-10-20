from peewee import *
import datetime
from event import *

db = SqliteDatabase('db/sempreverde.db')

class BaseModel(Model):
    class Meta:
        database = db

class SensorReading(BaseModel):
    id = AutoField()
    percentage = DoubleField()
    value = DoubleField()
    voltage = DoubleField()
    created_date = DateTimeField(default=datetime.datetime.now)

db.connect()
db.create_tables([SensorReading]) 
db.close()


class SensorRepository():
    def SaveReading(self, value, voltage, percentage):
        print(f"Reading: {percentage}%  | {voltage:4.2f}V ")
        db.connect()
        reading = SensorReading(percentage=percentage, value=value, voltage=voltage)
        reading.save()
        db.close()

    def __init__(self, event):
        db.connect()
        db.create_tables([SensorReading]) 
        db.close()
        event += self.SaveReading

