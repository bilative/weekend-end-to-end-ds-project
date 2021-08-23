from flask import Flask
from flask import jsonify
from flask import request
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('savFiles/basic_rfr_model.sav', 'rb'))
scaler = pickle.load(open('savFiles/scaler.sav', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getInfo():
    message = "This is REST API part of my weekend project!!"

    return jsonify({"message" : message}), 200


@app.route('/predict', methods=['POST'])
def postIdentity():
    data = request.get_json()
    new = pd.DataFrame({
        'age' : [data['age']],
        'Mil' : [data['Mil']],
        'Bodytype' : [data['Bodytype']],
        'Spoiler' : [data['Spoiler']],
        "Trim": [data['Trim']]
        })
    print(new)
    try:
        scaled = scaler.transform(new)
        data['Price'] = np.round(model.predict(scaled)[0], 2)
        return jsonify(data), 200
    except:
        return jsonify('There is a problem')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)