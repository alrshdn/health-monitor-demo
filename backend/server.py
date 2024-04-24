from datetime import datetime

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from pymongo import MongoClient


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
client = MongoClient("mongodb://172.18.0.2:27017/medical")
db = client["sensor_data"]


@app.route("/get_statistics", methods=["GET"])
@cross_origin()
def get_statistics():
    data = list(db.sensor_data.find({}, {"_id": False}))

    total = 0.0
    max_temp = data[0]["temparature"]
    for item in data:
        temp = item["temparature"]
        total += float(temp)
        if temp > max_temp:
            max_temp = temp

    avg = round((total / len(data)), 2)

    return jsonify([max_temp, str(avg)])


@app.route("/get_data", methods=["GET"])
@cross_origin()
def get_data():
    data = list(db.sensor_data.find({}, {"_id": False}))
    json_data = jsonify(data)
    return json_data


@app.route("/radera_data", methods=["GET"])
@cross_origin()
def radera_data():
    db.sensor_data.delete_many({})
    return ""


@app.route("/send_data", methods=["POST"])
def send_data():
    timestamp = request.args.get("timestamp")
    sensor_name = request.args.get("sensor_name")
    temparature = request.args.get("temparature")
    stress_level = request.args.get("stress_level")
    timezone = request.args.get("timezone")
    localtime = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    db.sensor_data.insert_one({
        "timestamp": timestamp,
        "sensor_name": sensor_name,
        "temparature": temparature,
        "stress_level": stress_level,
        "timezone": timezone,
        "localtime": localtime,
        })

    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

