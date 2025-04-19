import streamlit as st
import numpy as np
import joblib

# Load your trained model
model = joblib.load('air_quality_model.pkl')

st.title("Air Quality Prediction App 🌍")
st.write("This app predicts Carbon Monoxide (CO) concentration based on sensor input values.")

# Create input fields for the features
input1 = st.number_input('PT08.S1(CO) Sensor Reading')
input2 = st.number_input('NMHC(GT) Concentration')
input3 = st.number_input('C6H6(GT) Concentration')
input4 = st.number_input('PT08.S2(NMHC) Sensor Reading')
input5 = st.number_input('NOx(GT) Concentration')
input6 = st.number_input('PT08.S3(NOx) Sensor Reading')
input7 = st.number_input('NO2(GT) Concentration')
input8 = st.number_input('PT08.S4(NO2) Sensor Reading')
input9 = st.number_input('PT08.S5(O3) Sensor Reading')
input10 = st.number_input('Temperature')
input11 = st.number_input('Relative Humidity')
input12 = st.number_input('Absolute Humidity')

# Prepare input for prediction
input_features = np.array([[input1, input2, input3, input4, input5, input6,
                            input7, input8, input9, input10, input11, input12]])

if st.button("Predict CO Concentration"):
    result = model.predict(input_features)
    st.success(f"Predicted CO Concentration: {result[0]:.2f} mg/m³")
