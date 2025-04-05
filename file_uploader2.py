import streamlit as st

st.slider("this is the slider")

st.slider("This is the second slider2", min_value=40, max_value=200)

st.text_input("Enter your name here")

# for discriptive input from the user we have text area

st.text_area("Please discribe your text area")

st.date_input("Enter your learning date: ")

st.time_input("Enter your time here")