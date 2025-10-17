import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit")

st.write("This is a simple line text")

df=pd.DataFrame({
    'First Column':[1,2,3,4],
    'Second Column':[10,20,30,40]
})

st.write("Here is the dataframe")
st.write(df)

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.write("Here is the chart_data being displayed:")
st.write(chart_data)
st.line_chart(chart_data)