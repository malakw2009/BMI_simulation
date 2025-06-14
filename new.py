import streamlit as st

st.title('BMI calculator')

weight = st.number_input(
    label='Enter weight(kg):',
    min_value=10,
    max_value=300,
    value=50
)

height = st.number_input(
    label='Enter weight(m):',
    min_value=1.0,
    max_value=2.0,
    value=1.5,
    step=0.01
)

if st.button('Calculate'):
    bmi = weight/height ** 2
    st.write(f'Your BMI is: {bmi:.2f}')