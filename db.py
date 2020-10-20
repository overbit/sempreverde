from peewee import *
import datetime
# from pydispatch import dispatcher

db = SqliteDatabase('db/sempreverde.db')

class BaseModel(Model):
    class Meta:
        database = db

class SensorReading(BaseModel):
    id = AutoField()
    sensorName = CharField()
    value = DoubleField()
    voltage = DoubleField()
    created_date = DateTimeField(default=datetime.datetime.now)

def initDb():
    db.connect()
    db.create_tables([SensorReading]) 
    db.close()

if __name__ == '__main__':
    try:
        initDb()
    except Error as e:
        print(e)


# SIGNAL = 'my-first-signal'

# def handle_event( sender ):
#     """Simple event handler"""
#     print 'Signal was sent by', sender
# dispatcher.connect( handle_event, signal=SIGNAL, sender=dispatcher.Any )
# The