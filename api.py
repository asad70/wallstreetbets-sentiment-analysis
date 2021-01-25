from flask import Flask, jsonify
import Wallstreetbets
import json

app = Flask(__name__)

@app.route("/analyze")
def hello():
    print("Analyzing WallStreetBets")
    wsb = Wallstreetbets.analyze()
    wsb_object = json.dumps(wsb.__dict__)
    return wsb_object


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')