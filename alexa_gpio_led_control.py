from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging

GPIO.setmode(GPIO.BOARD)

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('LEDControlIntent', mapping={'color': 'color'})
def gpio_control(color):

    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)

    #GPIO.output(12, GPIO.HIGH)
    #turn on
    #GPIO.output(16, GPIO.LOW)
    if color in ['rot', 'red']:    
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
    elif color in ['grün', 'green']:    
        GPIO.output(12, GPIO.LOW)
        GPIO.output(16, GPIO.HIGH)

    return statement('Setze Farbe auf {}'.format(color))
