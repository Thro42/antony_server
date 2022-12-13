import io
import socket
import struct
import time
import threading
import fcntl
import sys
from flask import Flask, request, jsonify
from Motor import *
from servo import *
from Led import *
from Buzzer import *
from ADC import *
from Thread import *
from Light import *
from Ultrasonic import *
from Line_Tracking import *
from threading import Timer
from threading import Thread
from Command import COMMAND as cmd


class Antony:
    route_base = '/'
    def __init__(self):
        self.endChar='\n'
        self.LEDIndex= 0
        self.LEDred= 0
        self.LEDgreen= 0
        self.LEDblue= 0
        self.LedMoD=0
        self.left_Upper_Duty=0
        self.left_Lower_Duty=0
        self.right_Upper_Duty=0
        self.right_Lower_Duty=0
        self.channel=0
        self.angle=0
        self.sonic=True
        self.Light=False
        self.Mode = 'one'
        self.led=Led()
        self.ultrasonic=Ultrasonic()
        self.servo=Servo()
        self.PWM=Motor()

    def setLEDred(self, color):
        self.LEDred = color
        return self.buidResponse(self)
    def setLEDgreen(self, color):
        self.LEDgreen = color
        return self.buidResponse(self)
    def setLEDblue(self, color):
        self.LEDblue = color
        return self.buidResponse(self)

    def setLEDindex(self, index):
        self.LEDIndex = index
        return self.buidResponse(self)

    def setLEDcolor(self, red, green, blue):
        self.LEDred = red
        self.LEDgreen = green
        self.LEDblue = blue
        return self.buidResponse()

    def setLED(self, index, red, green, blue):
        self.LEDIndex = index
        self.LEDred = red
        self.LEDgreen = green
        self.LEDblue = blue
        self.led.ledIndex(self.LEDIndex,self.LEDred,self.LEDgreen,self.LEDblue)
        return self.buidResponse()

    def setLEDmode(self, mode):
        self.LedMoD = mode
        if self.LedMoD== '0':
            try:
                stop_thread(Led_Mode)
            except:
                pass
            self.led.ledMode(self.LedMoD)
            time.sleep(0.1)
            self.led.ledMode(self.LedMoD)
        else :
            try:
                stop_thread(Led_Mode)
            except:
                pass
            time.sleep(0.1)
            Led_Mode=Thread(target=self.led.ledMode,args=(mode,))
            Led_Mode.start()
        return self.buidResponse( )
    
    def setMotor(self, mot1,mot2,mot3,mot4):
        self.mot1=mot1
        self.mot2=mot2
        self.mot3=mot3
        self.mot4=mot4
        self.PWM.setMotorModel(mot1, mot2, mot3, mot4)
        return self.buidResponse( )


    def setSonic(self, state):
        if state == 'on':
            self.sonic=True
        elif state == 'off':
            self.sonic=False
        return self.buidResponse( )

    def setServo(self, channel, angle):
        self.channel=channel
        self.angle=angle
        self.servo.setServoPwm(channel,angle)
        return self.buidResponse( )
    
    def setLight(self, state):
        if state == 'on':
            self.Light=True
        elif state == 'off':
            self.Light=False
        return self.buidResponse( )
   



    def buidResponse(self):
        txtColor =  "#%02X%02X%02X" % (int(self.LEDred), int(self.LEDgreen), int(self.LEDblue))
        distance = 'off'
        self.adc=Adc()
        if self.sonic:
            ADC_Ultrasonic=self.ultrasonic.get_distance()
            distance=str(ADC_Ultrasonic)
        return jsonify( {
                'distance': distance,
                'color': txtColor,
                'LedMoD': self.LedMoD,
                'left_Upper_Duty': self.left_Upper_Duty,
                'left_Lower_Duty': self.left_Lower_Duty,
                'right_Upper_Duty': self.right_Upper_Duty,
                'right_Lower_Duty': self.right_Lower_Duty,
                'left': self.adc.recvADC(0),
                'right': self.adc.recvADC(1),
                })