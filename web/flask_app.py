import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
model_file = open("../model/model.pkl","rb")
model=pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    length1 = request.form.get('length1')
    length2 = request.form.get('length2')
    length3 = request.form.get('length3')
    height = request.form.get('height')
    width = request.form.get('width')
    input = [[length1, length2, length3, height, width]]
    prediction = model.predict(input)[0]
        
    return render_template('index.html', prediction_text=f'The estimated fish weight is {prediction:0.2f}')

if __name__=='__main__':
    app.run()