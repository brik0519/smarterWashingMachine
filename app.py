from flask import Flask, render_template, jsonify
import serial
import time

# 시리얼 통신 초기화
serialcom = serial.Serial('COM9', 9600)
serialcom.timeout = 1

app = Flask(__name__)

led_status = "UNKNOWN"

# LED 상태 확인 함수
def get_led_status():
    """시리얼 데이터를 읽어 LED 상태를 반환"""
    if serialcom.in_waiting > 0:  # 버퍼에 데이터가 있는 경우 읽기
        global led_status
        res = serialcom.readline()
        decoded_res = res.decode().strip()
        print(decoded_res)
        if "ON" in decoded_res.upper():
            led_status = "ON"
        elif "OFF" in decoded_res.upper():
            led_status = "OFF"
        # else: 
        #     led_status = led_status
    return  led_status # 데이터가 없거나 알 수 없는 상태

@app.route("/status")
def status():
    """현재 LED 상태 반환 (JSON)"""
    led_status = get_led_status()
    return jsonify(status=led_status)

@app.route("/", methods=['GET'])
def index():
    """LED 상태 표시"""
    led_status = get_led_status()  # LED 상태 동기화
    return render_template("index.html", status=led_status)

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0')
    finally:
        serialcom.close()  # 앱 종료 시 시리얼 통신 닫기
