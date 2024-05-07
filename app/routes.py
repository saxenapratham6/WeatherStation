from flask import render_template
from app import app
from app.data_collection import DataCollector
from app.data_storage import DataStorage
from app.data_transmission import DataTransmitter
from app.data_analysis import DataAnalyzer

@app.route('/')
def index():
    collector = DataCollector()
    storage = DataStorage()
    transmitter = DataTransmitter()
    analyzer = DataAnalyzer()

    data = collector.collect_data()
    storage.save_data(data)
    transmitter.transmit_data(data)
    analyzer.analyze_data(data)

    return render_template('index.html', temperature=data['temperature'], humidity=data['humidity'])
