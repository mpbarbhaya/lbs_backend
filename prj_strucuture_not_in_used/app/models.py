from app import db


class Meter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(50), nullable=False)
    data = db.relationship('MeterData', backref='meter', lazy=True)

    def __repr__(self):
        return f'<Meter {self.label}>'

class MeterData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meter_id = db.Column(db.Integer, db.ForeignKey('meter.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=True)
    value = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<MeterData {self.meter_id} {self.timestamp}>'