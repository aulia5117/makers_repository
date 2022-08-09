# Latihan 3
import requests, base64
from flask import Flask, request


app = Flask(__name__)

def BasicAuth() :
    pass_str = request.headers.get('Authorization')
    pass_bersih = pass_str.replace('Basic ',"")
    hasil_decode = base64.b64decode(pass_bersih)
    hasil_decode_bersih = hasil_decode.decode('utf-8')
    username_aja = hasil_decode_bersih.split(":")[0]
    pass_aja = hasil_decode_bersih.split(":")[1]
    if username_aja == 'tes' and pass_aja == 'tes123' :
        return True


@app.route('/weather')
def latihan3():
    if BasicAuth() :
        a = request.headers.get('city')
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={a}&appid=0af7650b00321f8081a8a9ad3a838f51')
        b = r.json()
        # return b
        
        return {
            'Weather' : b['weather'][0]['main'],
            'Coord' : b['coord'],
            'Temp' : b['main']['temp']
        } ,200
    else :
        return {
            '401' : 'Salah cuk'
        } , 401

# @app.route('/auth')

