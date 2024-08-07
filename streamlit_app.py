import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('My First Streamlit App')

# Display a dataframe
data = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
})
st.write(data)

# Add a slider
x = st.slider('Select a value')
st.write('Selected value:', x)

# Add a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)



import streamlit as st

st.title('Log In')

# Text input
name = st.text_input('Enter your name')
st.write(f'Hello, {name}!')

agee=st.text_input('ENter Your Age')
st.write(f'Your age,{agee}')
# Slider
age = st.slider('Select your age', 0, 100, 25)
st.write(f'Your age: {age}')

# Checkbox
agree = st.checkbox('I agree')
if agree:
    st.write('Thank you for agreeing!')

# Selectbox
favorite_color = st.selectbox('Select your favorite color', ['Red', 'Green', 'Blue'])
st.write(f'Your favorite color is {favorite_color}.')
