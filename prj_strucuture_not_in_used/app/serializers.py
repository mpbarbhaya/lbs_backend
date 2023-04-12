from marshmallow import Schema, fields

class MeterSchema(Schema):
    id = fields.Integer(dump_only=True)
    label = fields.String(required=True)

class MeterDataSchema(Schema):
    id = fields.Integer(dump_only=True)
    meter_id = fields.Integer(required=True)
    timestamp = fields.DateTime(dump_only=True)
    value = fields.Integer(required=True)