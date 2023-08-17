import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns 

application = Flask(__name__)
app=application

## import lasso scaler and standardscaler
lasso_model = pickle.load(open('models/Lasso.pkl','rb'))
standard_scaler = pickle.load(open('models/scaler.pkl','rb'))


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=="POST":
        pass
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")
