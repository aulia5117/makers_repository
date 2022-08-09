# Latihan 4

import requests, base64
from flask import Flask, request


app = Flask(__name__)

# def BasicAuth() :
#     pass_str = request.headers.get('Authorization')
#     pass_bersih = pass_str.replace('Basic ',"")
#     hasil_decode = base64.b64decode(pass_bersih)
#     hasil_decode_bersih = hasil_decode.decode('utf-8')
#     username_aja = hasil_decode_bersih.split(":")[0]
#     pass_aja = hasil_decode_bersih.split(":")[1]
#     if username_aja == 'tes' and pass_aja == 'tes123' :
#         return True


@app.route('/car-manufacturer',methods=["POST"])
def latihan4():
    # if BasicAuth() :
        r = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json')
        b = r.json()
        country_ = request.get_json()
        hasil = []
        # country = request.json['Results']['Country'] :
        country = b['Results']
        # return b
        for i in country :
            if i['Country'] == country_["Country"] :
                hasil.append(i["Mfr_Name"])
        return hasil
