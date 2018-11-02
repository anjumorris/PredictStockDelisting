from flask import Flask, abort, render_template, jsonify, request
from api import make_prediction
import numpy as np
import pandas as pd
import pickle

app = Flask('CompanyPredictApp')
company_list = pd.read_csv('./data/crystal_ball_web_ready.csv')

@app.route('/predict', methods=['POST'])
def do_prediction():
    if not request.json:
        abort(400)
    data = request.json
    #print(data);

    response = make_prediction(data, company_list)
    print(response)
    return jsonify(response)

@app.route('/get_company_list', methods=['POST'])
def get_list():
    #company_list = pd.read_csv('./data/crystal_ball_web_ready.csv')
    return jsonify(list(company_list['sa_company_name']))


@app.route('/')
def index():
    return render_template('index.html')

app.run()
