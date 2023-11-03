#!/usr/bin/env python3
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "flask"])

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/receiver", methods=["POST"])
def receiver():
    try:
        data = request.data.decode("utf-8")
        sanitized_data = data.replace("\r", "").replace("\n", "")
        print("Received data:", sanitized_data)
        return jsonify({"status": "success", "data": sanitized_data}), 200
    except Exception as e:
        print("An error occurred:", e)
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)
