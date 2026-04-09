import time
import requests
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False
while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone pressed the alert button!")
        button_pressed = True
        requests.get ("https://api.telegram.org/bot8790379477:AAHfnxpjzHuPf60SumRtaQK1e3-tDq1w7W0/sendmessage"),{"id": "8790379477","text": "Kingsley"}
    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False
    time.sleep(0.1)

