from flask import render_template, jsonify, views
from app import db
from app.models import Meter, MeterData
from app.serializers import MeterDataSchema

class MeterListView(views.MethodView):
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
    
class MeterDataView(views.MethodView):
    def get(self, pk):
        meter_data = MeterData.query.filter_by(meter_id=pk).order_by(MeterData.timestamp).all()
        meter_data_schema = MeterDataSchema(many=True)
        results = meter_data_schema.dump(meter_data)
        return jsonify(results)