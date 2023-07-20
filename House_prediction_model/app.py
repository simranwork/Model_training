import pickle
import numpy as np
import streamlit as st
import pandas as pd
import sklearn
ran = [1, 2, 3, 4, 5, 6, 7, 8]
data = pd.read_csv('final_result.csv')
area = data['location'].unique()
ran1 = data['bhk'].unique()

st.title("House Price Prediction in Bangalore")

model = pickle.load(open('RidgeModel.pkl', 'rb'))

location = st.selectbox("Select your Location", area)
input_bhk = st.selectbox("Enter Your BHK", ran)
input_bathroom = st.selectbox("Enter how many bathroom you required", ran1)
input_area = st.text_input("Enter the total square feet required")


def predict_price():
    input_ans = pd.DataFrame([[location, input_bhk, input_bathroom, input_area]], columns=['location', 'bhk', 'bath', 'total_sqft'])
    prediction = model.predict(input_ans)[0] * 100000

    return np.round(prediction, 1)


if st.button('Predict'):
    answer = predict_price()
    if answer <= 0:
        st.header("Property is not Available")
    else:
        st.header("₹ "+str(answer))
