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
    if request.method == 'POST':
        if 'on' in request.form.to_dict():
            serialcom.write(str('on').encode())
        if 'off' in request.form.to_dict():
            ledOff()
        
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host = '0.0.0.0')
