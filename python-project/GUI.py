import streamlit as st
import pandas as pd

data=pd.read_csv("GG.csv")
st.title("Mobile Prediction")
tab1, tab2, tab3 = st.tabs(["📈 Chart", "🗃 Data", "Prediction"])

with tab1:
    option = st.selectbox(
    'How would you like to be presented?',
    ('line_chart', 'chart2', 'chart3'))
    if option=="line_chart":
        for i in data.iloc[:,1:41].columns:
            st.line_chart(data[f"{i}"],y=i)
    elif option=="chart2":
        st.warning(option)
    else:
        st.error(option)
with tab2:
    st.subheader("A tab with the data")
    st.dataframe(data[:10])
