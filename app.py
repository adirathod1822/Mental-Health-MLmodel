import pickle
from flask import Flask, request, jsonify
import pandas as pd
app = Flask(__name__)

@app.route('/predict', methods=['GET'])

def predict():
    with open('model_pickle', 'rb') as file:
        model = pickle.load(file)
    f_lst = request.args.get("ip")
    lst = request.args.getlist("ip")
    array = [lst]
    df = pd.DataFrame(array,columns=['Age', 'Gender', 'family_history', 'benefits', 'care_options', 'anonymity', 'leave', 'work_interfere'])
    predictions = model.predict(df)
    d={}
    d['output'] = str(predictions[0])
    return d


if __name__ == '__main__':
    app.run()