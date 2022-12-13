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
        if direction == "right":
            return my_Server.antony.setMotor(-1500,-1500,1500,1500)
        elif direction == "left":
            return my_Server.antony.setMotor(1500,1500,-1500,-1500)
        elif direction == "backward":
            return my_Server.antony.setMotor(1500,1500,1500,1500)
        elif direction == "forward":
            return my_Server.antony.setMotor(-1500,-1500,-1500,-1500)
        elif direction == "stop":
            return my_Server.antony.setMotor(0,0,0,0)
        else:
            return my_Server.antony.buidResponse()
    
class setLedMode(Resource):
    def get(self,mode):
        return my_Server.antony.setLEDmode(mode)

class setSonic(Resource):
    def get(self,state):
        return my_Server.antony.setSonic(state)
class setServo(Resource):
    def get(self,channel, angle):
        return my_Server.antony. setServo(channel, angle)
class setLight(Resource):
    def get(self,state):
        return my_Server.antony. setLight(state)

       