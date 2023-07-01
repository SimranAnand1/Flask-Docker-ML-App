from flask import Flask,render_template,url_for,request
import pandas as pd 
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib


app = Flask(__name__)
model = pickle.load(open('NB_spam_model.pkl','rb'))

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():

    cv = CountVectorizer()
    # joblib.dump(model, 'NB_spam_model.pkl')
    # NB_spam_model = open('NB_spam_model.pkl','rb')
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = model.predict(vect)
       
    return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)