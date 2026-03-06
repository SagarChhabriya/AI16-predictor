import streamlit as st 
import pickle

st.set_page_config(page_title="Income Predictor", page_icon="💵")
st.title("Income Predictor 💵")

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

yoe = st.number_input("Enter Years of Experience", min_value=0.0, max_value=11.0, step=0.5, value=1.0)

if st.button("Predict"):
    predictions =  model.predict([[yoe]])
    st.success(predictions)