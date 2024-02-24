# Import libraries
import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained model
model = joblib.load('tree_model.joblib')

# App logo
logo = "logo_two.webp"
st.image(logo, width=300)

# App title
st.title('Height Prediction App (CCTH)')
st.write("Height prediction tool for patients at the Cape Coast Teaching Hospital, Ghana")

st.markdown("*Email*:  ankueric1@gmail.com")

# User inputs
gender = st.selectbox('Sex', ['Male', 'Female'])
mean_ulna = st.number_input('Ulna Length (cm)', min_value=20.0, step=1.0)
age = st.number_input('Age (years)', min_value=18, step=1)

# Binary sex output
gender = 0 if gender == 'Male' else 1

# Prepare the input array with one-hot encoding for 'Sex'
#inputs = np.array([[age, gender, mean_ulna]])
inputs = np.array([[age, gender, mean_ulna]])

# Assuming `np_array_to_predict` is your NumPy array for prediction
df_predict = pd.DataFrame(inputs, columns=['age', 'gender', 'mean_ulna'])

# Button for prediction
if st.button('Predict'):
    # Perform prediction
    prediction = model.predict(df_predict)
    
    # Display the prediction
    st.write(f'Predicted height: {round(prediction[0], 1)} cm')
