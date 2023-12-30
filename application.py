import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time as t

pickle_in=open('mines_classification.pkl','rb')
model=pickle.load(pickle_in)

st.title('Mines Classification')
st.text("Note:Mines above height of 1 cm  are most probably connected to booby traps ")
v=float(st.slider("Enter the  Voltage(v)",0.0,10.6))

h=float(st.slider("Enter the  High(H) in cm",0.0,20.0))

k=st.selectbox("Select the soil type",['Dry and Sandy','Dry and Humpy','Dry and Limy','Humid and Sandy','Humid and Humus','Humid and Limy'])

btn=st.button("Classify")
if k=='Dry and Sandy':
    s=0
elif k=='Dry and Humpy':
    s=0.2
elif k=='Dry and Limy':
    s=0.4
elif k=='Humid and Sandy':
    s=0.6
elif k=='Humid and Humus':
    s=0.8
elif k=='Humid and Limy':
    s=1

if btn:
    st.text("Model is Classifying")
    # t.sleep(5)
    input=np.array([[v,h,s]]).astype(np.float64)
    prediction=model.predict(input)
    if prediction==1:
        st.text("NUll")
    elif prediction==2:
        st.text("Mine is Anti-Tank type")
    elif prediction==3:
        st.text("Mine is Anti-personnel type")
    elif prediction==4:
        st.text("Mine is Booby Trapped Anti-personnel type")
    elif prediction==5:
        st.text("Mine is M14 Anti_personnel type")
    st.image('land_mine.jpg')
        






