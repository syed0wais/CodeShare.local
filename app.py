from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
shared_code = ""  # In-memory storage

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    global shared_code
    shared_code = request.json.get("code", "")
    return jsonify({"status": "ok"})

@app.route("/get", methods=["GET"])
def get():
    return jsonify({"code": shared_code})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

