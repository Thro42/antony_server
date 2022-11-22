from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from Antony import *
#from . import antony

class Server:
  def __init__(self):
    self.antony = Antony()

my_Server = Server()
#antony = Antony

class getStatus(Resource):
    def get(self):
        return my_Server.antony.buidResponse()

class setColor(Resource):
    def get(self,red_id,green_id,blue_id):
        return my_Server.antony.setLEDcolor(red_id, green_id, blue_id)
class setMotor(Resource):
    def get(self,mot1,mot2,mot3,mot4):
        return my_Server.antony.setMotor(mot1,mot2,mot3,mot4)
class setDirection(Resource):
    def get(self,direction):
        match direction:
            case "left":
                return my_Server.antony.setMotor(-1500,-1500,1500,1500)
            case "right":
                return my_Server.antony.setMotor(1500,1500,-1500,-1500)
            case "forward":
                return my_Server.antony.setMotor(1500,1500,1500,1500)
            case "backward":
                return my_Server.antony.setMotor(-1500,-1500,-1500,-1500)
            case "stop":
                return my_Server.antony.setMotor(0,0,0,0)
