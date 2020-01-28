from Utilities.config import db

class Data(db.Model):
    __tablename__="data"
    timestamp=db.Column(db.DateTime,primary_key=True)
    temp=db.Column(db.Float)
    humidity=db.Column(db.Float)


def receiveData(data):
    timestamp=data['timestamp']
    temp=data['temperature']
    humidity=data['humidity']

    record=Data(timestamp=timestamp,temp=temp,humidity=humidity)
    db.session.add(record)
    db.session.commit()
    return "data added successfully"