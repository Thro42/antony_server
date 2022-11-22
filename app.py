# app.py
import  sys
import threading
from flask import Flask, request, jsonify
from Antony import *
from Server import *
from flask_restful import Api, Resource, reqparse, fields, marshal

app = Flask(__name__)
api = Api(app)
antony = Antony

api.add_resource(getStatus, '/', )
api.add_resource(setColor, '/color/<red_id>/<green_id>/<blue_id>', )
api.add_resource(setMotor, '/motor/<mot1>/<mot2>/<mot3>/<mot4>', )
api.add_resource(setDirection, '/direction/<direction>', )

if __name__ == '__main__':
    app.run()