from flask import Blueprint, jsonify, request
from app.weather import get_weather, get_forecast
import os


main_bp= Blueprint('main', __name__)

@main_bp.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

@main_bp.route('/api/weather/<city>', methods=['GET'])
def weather(city):
    try:
        data = get_weather(city)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error':str(e)}), 400


@main_bp.route('/api/forecast/<city>', methods=['GET'])
def forecast(city):
    try:
        data = get_forecast(city)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if  __name__=='__main__':
    from app import create_app
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
