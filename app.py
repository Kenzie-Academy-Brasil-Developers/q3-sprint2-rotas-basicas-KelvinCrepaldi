# Código do dev aqui
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return {'data': "Hello Flask!"}

@app.route('/current_datetime')
def current_datetime():
    datetime_now = datetime.now()
    datetime_formated = datetime_now.strftime("%d/%m/%Y %H:%M:%S %p")
    hour = int(datetime_now.strftime("%H"))

    if(hour < 12):
        message="Bom dia!"
    elif(hour < 18):
        message="Boa tarde!"
    else:
        message="Boa noite!"


    return { 'current_datetime': datetime_formated, 'message': message}