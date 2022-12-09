# https://stackoverflow.com/questions/43205568/python-flask-server-with-mqtt-subscription

from flask import Flask, render_template, jsonify
import paho.mqtt.client as mqtt
import mosquitto_mqtt_pi
import read_csvfile
import random

port = 5000

app = Flask(__name__)
port = 5000
sensor_value = 0

@app.route('/')
def render_mainpage():
    return render_template('index.html', name="nakyeonko")

@app.route('/getSensorData')
def getSensorData():
    return jsonify({'sensor_data':random.randint(100, 1024)})

@app.route('/getPHSensorData')
def getPHSensorData():
    sensor_value = float(read_csvfile.get_senor_data_last_value())
    return jsonify({'sensor_data':sensor_value})

if __name__ == '__main__':
    mosquitto_mqtt_pi.mqtt_init()
    app.run(host='0.0.0.0', port=port, debug=True)