import streamlit as st
import pandas as pd

st.title("Streamlit Widget page")

name=st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! Welcome to this Streamlit App")

age=st.slider("Select your Age:",0,100,25)
st.write(f"{name}'s age is {age}.")

opt=["Python","Java","C",'C++','JavaScript']
ch=st.selectbox("Choose the Language:", opt)
st.write(f"You selected {ch}.")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

upload_file=st.file_uploader("Choose a CSV file",type='csv')

if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.write(df)
else:
    st.write("Error: Incorrect Option selected.")
    st.write("Info: Choose a CSV file")