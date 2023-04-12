from flask import Flask, jsonify
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lbs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)


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



@app.before_first_request
def add_fake_data():
    meter1 = Meter(label='Meter 1')
    meter2 = Meter(label='Meter 2')
    db.session.add_all([meter1,meter2])
    db.session.commit()

    meter1_data = [MeterData(meter_id=meter1.id, value=i) for i in range(10)]
    db.session.add_all(meter1_data)
    db.session.commit()

    meter2_data = [MeterData(meter_id=meter2.id, value=i) for i in range(10)]
    db.session.add_all(meter2_data)
    db.session.commit()


class MeterSchema(Schema):
    id = fields.Integer(dump_only=True)
    label = fields.String(required=True)

class MeterDataSchema(Schema):
    id = fields.Integer(dump_only=True)
    meter_id = fields.Integer(required=True)
    timestamp = fields.DateTime(dump_only=True)
    value = fields.Integer(required=True)


class MeterListView(MethodView):
    def get(self):
        meters = Meter.query.all()
        results = []
        for i in meters:
            meter_data = {
                'id':i.id,
                'label':i.label,
                'link':f'/meters/{i.id}/'
            }
            results.append(meter_data)
        return jsonify(results)
    
class MeterDataView(MethodView):
    def get(self, pk):
        meter_data = MeterData.query.filter_by(meter_id=pk).order_by(MeterData.timestamp).all()
        meter_data_schema = MeterDataSchema(many=True)
        results = meter_data_schema.dump(meter_data)
        return jsonify(results)
    
app.add_url_rule('/meters/', view_func=MeterListView.as_view('meter_list'))
app.add_url_rule('/meters/<int:pk>/', view_func=MeterDataView.as_view('meter_data'))


if __name__ == '__main__':
    app.run(debug=True)