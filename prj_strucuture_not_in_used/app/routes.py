from flask import Blueprint
from .views import MeterListView, MeterDataView
from app import create_app

api_blueprint =Blueprint('api', __name__)

# app = create_app()
api_blueprint.add_url_rule('/meters/', view_func=MeterListView.as_view('meter_list'))
api_blueprint.add_url_rule('/meters/<int:pk>/', view_func=MeterDataView.as_view('meter_data'))