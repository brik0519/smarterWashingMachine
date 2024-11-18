from flask import Flask, render_template, Response, request
import serial
import time

serialcom = serial.Serial('COM9', 9600)
serialcom.timeout = 1

app = Flask(__name__)

def ledOn():
    serialcom.write(str('on').encode())

def ledOff():
    serialcom.write(str('off').encode())

def disconnect():
    serialcom.close()

@app.route("/", methods=['GET', 'POST'])
def index():
    led_status = "OFF"
    if serialcom.readable():
        res = serialcom.readline()
        decoded_res = res.decode().strip()  # 디코딩 후 앞뒤 공백 제거
    print(decoded_res[:len(decoded_res) - 1])

    if "ON" in decoded_res.upper():
        led_status = "ON"

    elif "OFF" in decoded_res.upper():
        led_status = "OFF"
    # if request.method == 'POST':
    #     if 'on' in request.form.to_dict():
    #         serialcom.write(str('on').encode())
    #     if 'off' in request.form.to_dict():
    #         ledOff()
        
    return {"status": led_status}  # JSON 형태로 반환
    
if __name__ == "__main__":
    app.run(host = '0.0.0.0')
