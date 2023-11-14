import streamlit as st
import numpy as np
import pandas as pd
import pickle



model=pickle.load(open('model.pkl','rb'))
st.title("Ticket Booking Prediction")
st.image("modelbanner.png")


nav = st.sidebar.radio("Navigation",["Aim","Prediction"])      

if nav == 'Aim':
    st.markdown(""" #### Aim of the Project """)

    

def Predict_buy(x1,x2,x3,x4,x5,x16,x17,x18):
    x6 = int(x16)
    x7 = int(x17)
    x8 = int(x18)
    input=np.array([[x1,x2,x3,x4,x5,x6,x7,x8]]).astype(np.float64)
    prediction=model.predict(input)
    pred=prediction[0]
    return pred


if nav == 'Prediction':
    
    st.header('Will Customer Buy the Ticket?')
    
    val1 = st.text_input('Purchase lead')
    val2 = st.text_input('Flight Hour')
    val3 = st.text_input('Length of Stay')
    val4 = st.text_input('Flight Duration')
    val5 = st.text_input('Flgith Day')
    ques1 = st.radio(

    "Does Customer wants Meals on Flight",

    ('No','Yes'))

    if ques1 == 'Yes':
        val6 = True

    if ques1 == 'No':
        val6 = False

    ques2 = st.radio(

    "Does Customer have Extra Baggage",

    ('No','Yes'))

    if ques2 == 'Yes':
        val7 = True

    if ques2 == 'No':
        val7 = False

    ques3 = st.radio(

    "Does Customer have Seat Prefference",

    ('No','Yes'))

    if ques3 == 'Yes':
        val8 = True

    if ques3 == 'No':
        val8 = False


    





    if st.button("Predict"):
        value = Predict_buy(val1,val2,val3,val4,val5,val6,val7,val8)
        if value == False:
            st.success('Not Buying the Ticket')
        if value == True:
            st.success('Buy the Ticket')
    