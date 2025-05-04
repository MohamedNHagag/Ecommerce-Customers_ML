import streamlit as st
import joblib
import numpy as np
import pandas as pd

# تحميل المودل

model = joblib.load(r"D:\data science\7)machine learning\projects\project 1\model.pkl")
st.title('prediction Yearly Amount Spent')
st.info('Esay application for predict amount spent at year')
st.sidebar.header('hello in the app')


Avg_Session_Length=st.text_input('Avg. Session Length')
TimeonApp=st.text_input('Time on App')
TimeonWebsite=st.text_input('Time on Website')
LengthofMembership=st.text_input('Length of Membership')

#convert data_into to data frame
df = pd.DataFrame({
    'Avg. Session Length': [Avg_Session_Length], 
    'Time on App': [TimeonApp], 
    'Time on Website': [TimeonWebsite], 
    'Length of Membership': [LengthofMembership]
},index=[0])

button_confirm=st.sidebar.button('confirm')
if button_confirm:
    result=model.predict(df)
    st.sidebar.write(result)

