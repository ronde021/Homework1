(* PY File *)
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

hitPoints = 20
interactions = []

@app.route('/hpt/getHP',methods=['GET'])
def getHP():
    return jsonify({"Hitpoints":hitPoints});

@app.route('/hpt/getHistory',methods=['GET'])
def getHistory():
    return jsonify(interactions);

@app.route('/hpt/addHP',methods=['POST'])
def addHP():
    global hitPoints
    interaction = request.getjson()
    interaction["type"] = "add"
    interaction["time"] = datetime.now()
    hitPoints += interaction["amount"]
    interactions.append(interaction)
    return jsonify({"Hitpoints":hitPoints})

@app.route('/hpt/reduceHP',method=['POST'])
def reduceHP():
    global hitPoints
    interaction = request.getjson()
    interaction["type"] = "reduce"
    interaction["time"] = datetime.now()
    hitPoints -= interaction["amount"]
    interactions.append(interaction)
    return jsonify({"Hitpoints":hitPoints})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8090,debug=True)
