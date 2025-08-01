import streamlit as st
import numpy as np
import joblib  

# Load model
model = joblib.load("Farm_Irrigation_System.pkl")

# Set wide layout and page config
st.set_page_config(page_title="Smart Sprinkler System", layout="wide")

# ------------------ Header ------------------
st.markdown("""
    <div style="background-color:#1f5c3f;padding:20px;border-radius:10px">
        <h1 style="color:white;text-align:center;"> Smart Sprinkler System</h1>
        <p style="color:white;text-align:center;font-size:18px;">
            Predict which sprinkler units need to be turned ON or OFF using real-time sensor data 
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("")

# ------------------ Input Section ------------------
st.markdown("###  Input Sensor Values")
st.markdown("Use the sliders below to simulate scaled sensor data (between 0 and 1):")

sensor_values = []
cols = st.columns(4)

for i in range(20):
    with cols[i % 4]:
        val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        sensor_values.append(val)

# ------------------ Prediction ------------------
st.markdown("---")
predict = st.button(" Predict Sprinkler Status")

if predict:
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("##  Prediction Results")
    st.markdown("Sprinkler status based on the given sensor inputs:")

    result_cols = st.columns(4)

    for i, status in enumerate(prediction):
        color = "#28a745" if status == 1 else "#dc3545"
        emoji = " ON" if status == 1 else " OFF"
        result_cols[i % 4].markdown(
            f"""
            <div style='
                background-color:{color};
                padding:20px;
                margin:5px 0;
                border-radius:10px;
                text-align:center;
                color:white;
                font-weight:bold;
                font-size:16px;'
            >
                Sprinkler {i} <br> {emoji}
            </div>
            """, unsafe_allow_html=True
        )

# ------------------ Footer ------------------
st.markdown("---")
st.markdown("""
    <div style="text-align:center;font-size:14px;color:gray;">
        Developed as part of the Smart Irrigation Project  | Powered by Machine Learning & Streamlit
    </div>
""", unsafe_allow_html=True)
