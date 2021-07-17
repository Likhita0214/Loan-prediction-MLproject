# To run this file type following in cmd
# streamlit run prog_name.py

import streamlit as st
#from PIL import Image
import pickle

model=pickle.load(open("ML_Model1","rb"))

#im=Image.open('pred.png')
#im=im.resize((150*2,150))
#st.image(im,use_column_width=False)
#st.title("Loan Prediction")

ID=st.text_input("Account Number")

name=st.text_input("Name")

g=('Female','Male')
gen=st.selectbox("Gender",[0,1],format_func=lambda x: g[x])

m=('No','Yes')
mar=st.selectbox("Married?",[0,1],format_func=lambda x: m[x])

d=('0','1','2','more than 3')
dep=st.selectbox("No.of Dependents",[0,1,2,3],format_func=lambda x:d[x])

e=('Ungraduated','Graduated')
Edu=st.selectbox("Education",[0,1],format_func=lambda x:e[x])

SE=st.selectbox("Are you self employed?",[0,1],format_func=lambda x:m[x])

ApIncome=st.number_input("Applicant Income")

CoIncome=st.number_input("Coapplicant Income")

LAmount=st.number_input("Loan Amount")

time=("2 months","6 months","8 months","1 year","16 months")
LTerm=st.selectbox("Time period",[0,1,2,3,4],format_func=lambda x:time[x])

c=(0.0,1.0)
CH=st.selectbox("Credit History",[0,1],format_func=lambda x:c[x])

p=["Rural","Semi-Urban","Urban"]
prop=st.selectbox("Property Area",[0,1,2],format_func=lambda x:p[x])

if st.button('Predict'):
    duration=0
    if LTerm==0:
        duration=60
    if LTerm==1:
        duration=180
    if LTerm==2:
        duration=240
    if LTerm==3:
        duration=360
    if LTerm==4:
        duration=480
    l=[[gen,mar,dep,Edu,SE,ApIncome,CoIncome,LAmount,duration,CH,prop]]
    prediction=model.predict(l)
    if str(prediction[0])=='1':
        st.success("Hello : "+name+"\n"+"Account Number : "+ID+"\nCongratulation ! You can get the loan")
    else:
        st.error("Hello : "+name+"\nAccount Number : "+ID+"\n Sorry ! You cannot get the loan as per our prediction")
      

