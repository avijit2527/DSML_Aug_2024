import streamlit as st

st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="gray")
st.header("These headers have rotating dividers", divider=True)
st.header("One", divider=True)
st.header("Two", divider=True)
st.header("Three", divider=True)
st.header("Four", divider=True)

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

import streamlit as st

agree = st.checkbox("Do you agree?")

if agree:
    st.write("You agreed!")
else:
    st.write("You did not agree!")