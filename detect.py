from flask import Flask, render_template, Response, request
import serial
import time

serialcom = serial.Serial('COM9', 9600)
serialcom.timeout = 1

while(1):
    led_status = "OFF"
    if serialcom.readable():
        res = serialcom.readline()
        decoded_res = res.decode().strip()  # 디코딩 후 앞뒤 공백 제거
    print(decoded_res[:len(decoded_res) - 1])

    if "ON" or "RUN" in decoded_res.upper():
            led_status = "ON"