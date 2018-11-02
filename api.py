import numpy as np
import pandas as pd
import pickle

pipeline = pickle.load(open('./model/model_pickles/best_rf.pkl', 'rb'))

c_b = {}
example = {
  'Company': '20 MICRONS LTD.',  # int
  }

def make_prediction(features, crystal_ball):
    #crystal_ball = pd.read_csv('./data/crystal_ball_web_ready.csv')
    company_name=features['Company']
    pull_out = crystal_ball.loc[crystal_ball['sa_company_name']==company_name,'sa_total_income':]
    X = np.array(pull_out)
    prob_delisted = pipeline.predict_proba(X)[0, 1]

    result = {
        'prediction': int(prob_delisted > 0.15),
        'prob_delisted': prob_delisted
    }
    return result


if __name__ == '__main__':
    print(make_prediction(example , c_b))
