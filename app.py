from flask import Flask, render_template, request
import pandas as pd
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])

def predict():

    basename = "file"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([basename, suffix])

    pclass = request.form['Pclass']
    sex = request.form['Sex']
    age = request.form['Age']
    sibsp = request.form['SibSp']
    parch = request.form['Parch']
    embarked = request.form['Parch']

    data = [[pclass, sex, age, sibsp, parch, embarked]]
    df = pd.DataFrame(data, columns=['Pclass', 'Sex','Age','SibSp','Parch','Embarked'])
    df.to_csv(f'csv_files/{filename}.csv')

    return render_template('index.html')

