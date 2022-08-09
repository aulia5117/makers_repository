# Latihan 5

from flask import Flask, request

app = Flask(__name__)

@app.route("/picking-numbers", methods=["PUT"])
def pickingNumbers():
    # Write your code here
    data =  request.get_json()
    a = request.json['a']
    # return a

    wadah_count = [0]*max(a)
    for i in a :
        wadah_count[i-1] += 1
    count = wadah_count[0] + wadah_count[1]

    for i in range(len(wadah_count)) : 
        if count < wadah_count[i-1] + wadah_count[i] :
            count = wadah_count[i-1] + wadah_count[i] 

    return {
        "hasil" : count
    }