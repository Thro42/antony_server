from flask import Flask, request, jsonify


class Antony:
    route_base = '/'
    def __init__(self):
        self.endChar='\n'
        self.LEDColor= 0
        self.LEDred= 0
        self.LEDgreen= 0
        self.LEDblue= 0
        self.left_Upper_Duty=0
        self.left_Lower_Duty=0
        self.right_Upper_Duty=0
        self.right_Lower_Duty=0

    def setLEDred(self, color):
        self.LEDred = color
        return self.buidResponse(self)
    def setLEDgreen(self, color):
        self.LEDgreen = color
        return self.buidResponse(self)
    def setLEDblue(self, color):
        self.LEDblue = color
        return self.buidResponse(self)

    def setLEDcolor(self, red, green, blue):
        self.LEDred = red
        self.LEDgreen = green
        self.LEDblue = blue
        return self.buidResponse()

    def setMotor(self, mod1,mod2,mod3,mod4):
        self.left_Upper_Duty=mod1
        self.left_Lower_Duty=mod2
        self.right_Upper_Duty=mod3
        self.right_Lower_Duty=mod4
        return self.buidResponse()

    def buidResponse(self):
        txtColor =  "#%02X%02X%02X" % (int(self.LEDred), int(self.LEDgreen), int(self.LEDblue))
        return jsonify( {
                'color': txtColor,
                'left_Upper_Duty': self.left_Upper_Duty,
                'left_Lower_Duty': self.left_Lower_Duty,
                'right_Upper_Duty': self.right_Upper_Duty,
                'right_Lower_Duty': self.right_Lower_Duty
                })