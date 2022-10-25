# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/move_forward")
def move_forward():
    moving = "movin Forward"
    return moving, 201

@app.route("/motors", methods=['GET'])
def motors():
    m1 = request.args.get('m1')
    m2 = request.args.get('m2')
    m3 = request.args.get('m3')
    m4 = request.args.get('m4')
    print( "self.PWM.setMotorModel(" + m1 + "," +m2+","+m3+","+m4+")")
    return "OK", 201

@app.route("/move", methods=['GET'])
def move():
    dir = request.args.get('dir')
    moving = "movin " + dir
    if dir == "left":
        moving = "Also nach links"
        print("self.PWM.setMotorModel(-1500,-1500,1500,1500)")
    if dir == "right":
        moving = "Liber nach rechts"
        print("self.PWM.setMotorModel(1500,1500,-1500,-1500)")
    return moving, 201

