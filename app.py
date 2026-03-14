from flask import Flask, request, jsonify

app = Flask(__name__)

devices = {}


# -----------------------------
# Upload endpoint (device -> cloud)
# -----------------------------
@app.route("/api/upload", methods=["POST"])
def upload():

    data = request.json

    device_id = data.get("device_id")

    devices[device_id] = data

    return {"status": "stored"}


# -----------------------------
# Get latest readings
# -----------------------------
@app.route("/api/readings")
def readings():

    return jsonify(devices)


# -----------------------------
# Get specific device
# -----------------------------
@app.route("/api/device/<device_id>")
def device(device_id):

    return jsonify(devices.get(device_id, {}))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)