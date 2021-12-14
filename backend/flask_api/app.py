from flask import Flask, jsonify
from mysql import database
HOST = '0.0.0.0'; PORT=3005

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return jsonify({"statusCode": 200, "res": "Hello World"})
@app.route('/register', methods=["POST"])
def register():
    db = database()
    db.connect()
    db.disconnect()
    return

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
