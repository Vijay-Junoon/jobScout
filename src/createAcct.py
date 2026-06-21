import streamlit as st
from tools.databaseHandler import put


def createAccount(name,email,pwd,jobrole,exp,loc,sal):
  print(put(name,email,pwd,jobrole,exp,loc,float(sal)))


name = st.text_input("Name",key = "name")
email = st.text_input("Email Address",key = "email")
pwd = st.text_input("Password",key="password")
jobRole = st.text_input("Job Role",key = "jobRole")
exp = st.slider("Experience",min_value=0,max_value = 35)
loc = st.text_input("Location",key = "location")
salary = st.slider("Expected Salary",min_value=0,max_value=1000000)

createAccountButton = st.button("Create Account",on_click = lambda: createAccount(name,email,pwd,jobRole,exp,loc,salary))