# 🌍 Air Quality Prediction Project

This project uses the **UCI Air Quality Dataset** to predict **Carbon Monoxide (CO) concentrations** based on other air pollutant sensor readings, using Python, scikit-learn, and Streamlit.

---

## 📌 About the Dataset

The dataset was sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/360/air+quality).  
It contains hourly averaged responses from an array of chemical sensors deployed in Italy, along with weather conditions like Temperature and Humidity.

---

## 🧠 Machine Learning Model

- Model Type: `Linear Regression`
- Goal: Predict the `CO(GT)` (Carbon Monoxide) value using other available sensor features.
- Libraries used: `pandas`, `numpy`, `scikit-learn`, `joblib`.

---

## 💻 Web Application

A simple and interactive Streamlit web app allows users to:
- Enter new sensor values.
- Predict the expected **CO concentration**.
- Display the result instantly.

To run the app locally:

```bash
streamlit run app.py
