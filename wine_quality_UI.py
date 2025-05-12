import streamlit as st
import numpy as np
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

st.title("Wine-quality Prediction")

prompts = {
    "fixed_acidity": st.number_input,
    "volatile_acidity": st.number_input,
    "citric_acid": st.number_input,
    "residual_sugar": st.number_input,
    "chlorides": st.number_input,
    "free_sulfur_dioxide": st.number_input,
    "total_sulfur_dioxide": st.number_input,
    "density": st.number_input,
    "pH": st.number_input,
    "sulphates": st.number_input,
    "alcohol": st.number_input,

}

with st.form("features"):
    features = [fn(p) for p, fn in prompts.items()]
    if st.form_submit_button("Submit"):
        features = np.array(features).reshape(1, -1)
        obj = PredictionPipeline()
        pred = obj.predict(features)
        st.markdown(f"Wine-Quality Prediction is: {round(pred[0])}/8")