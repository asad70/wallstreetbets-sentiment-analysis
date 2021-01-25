from flask import Flask, jsonify
import Wallstreetbets
import json
import os

clientid = os.getenv('CLIENT_ID')
clientsecret = os.getenv('CLIENT_SECRET')
usernme = os.getenv('USERNAME')
passwrd = os.getenv('PASSWORD')

app = Flask(__name__)

@app.route("/analyze")
def hello():
    print("Analyzing WallStreetBets")
    wsb = Wallstreetbets.analyze(clientid, clientsecret, usernme, passwrd)
    wsb_object = json.dumps(wsb.__dict__)
    return wsb_object


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')