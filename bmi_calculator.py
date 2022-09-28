import streamlit as st
from PIL import Image

st.set_page_config(
   page_title="BMI Calculator",
#    initial_sidebar_state="expanded",
)

st.title("Body Mass Index Calculator")
st.write("Body Mass Index (BMI) is calculated by dividing a person's weight in kilograms (or pounds) by their height in meters squared (or feet). A high BMI might suggest excessive body fat. BMI tests for weight categories that may contribute to health concerns but does not assess an individual's body fatness or health.")

st.subheader("Metric BMI Formula")
st.latex('''
        BMI = weight(kg)/(height(m))^2
        ''')

with st.expander("BMI Interpretation"):
    st.caption("This table shows the corresponding interpretation of certain BMI within a range.")
    image = Image.open('bmi_classification.jpg')
    st.image(image, caption='BMI Interpretation')

def categorize(bmi):
    if bmi <= 18.5:
        return "UNDERWEIGHT"
    elif bmi >= 18.5 and bmi <= 24.90:
        return "NORMAL WEIGHT"
    elif bmi >= 24.91 and bmi <= 29.99:
        return "OVERWEIGHT"
    else: 
        return "OBESE"

st.markdown('---')
weight = st.number_input("Weight in kilograms (kg): ")
height = st.number_input("Height in meters (m): ")

try:
    bmi = round(weight / height ** 2, 2)
    st.subheader('Body Mass Index')
    st.write(f"""
        BMI: {bmi}\n
        Weight: {weight} kg\n
        Height: {height} m\n
        Interpretation: **{categorize(bmi)}**
        """)
except (ZeroDivisionError, NameError):
    pass

st.markdown('---')
st.caption("**Reference:**")
st.caption("Centers for Disease Control and Prevention. (2022). *Body mass index (BMI).* Centers for Disease Control and Prevention. Retrieved from https://www.cdc.gov/healthyweight/assessing/bmi/index.html ")