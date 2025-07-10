import streamlit as st
import joblib
import numpy as np


model = joblib.load("model.pkl")


st.title("HOUSE PRICE PREDICTION APP")

st.divider()

st.write("This app uses machine learning for predicting house price with given features of the house. For using this app you enter the inputs from this UI and then use predict button.")

st.divider()

bedrooms = st.number_input("Number of bedrooms", min_value = 0, value = 0)
bathrooms = st.number_input("Number of bathrooms", min_value = 0, value = 0)
livingarea = st.number_input("Living area", min_value = 0, value = 2000)
condition = st.number_input("Conditions", min_value = 0, value = 3)
numberofschools = st.number_input("Number of schools nearby", min_value = 0, value = 0)

st.divider()

X = [[bedrooms,bathrooms,livingarea,condition,numberofschools]]




if st.button("🚀 Predict!"):


    if all(x == 0 for x in X[0]):
        st.warning("⚠️ Please enter meaningful, non-zero values.")
    else:
        prediction = model.predict(X)
        st.balloons()
        st.success(f"🏷️ Predicted house price: ₹{prediction[0]:,.2f}")





#'number of bedrooms', 'number of bathrooms', 'living area','condition of the house', 'Number of schools nearby'