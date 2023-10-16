import streamlit as st
import time as t


#creating title for the application
st.title("Welcome to my web application")

# Header
st.header("Machine learning")

# Sub-Header
st.subheader("Linear Regression")

# To give information
st.info("information details of a user")

# To give a warning message
st.warning("use algorithms for effeciency")

# To write messages
st.write("Employee name")
# For error message
st.error("wrong password")

# Success message
st.success("congratulations surya, you have got a good job in chennai as a software developer surya")
st.success("you have completed your internship successfully by improving your skillset very much")

# Markdown
st.markdown("intellipat")
st.markdown("# intellipat")
st.markdown("## intellipat")
st.markdown(":moon:")

# To write a caption 
st.caption("Caption is here")

# To display a mathematical function
st.latex(r'''a+b x^2+c''')

# To add an image
st.image("download.png")

# Widgets 
# To create a check box
st.checkbox("Login")

#To create a button
st.button("click")

#To create a radio widget
st.radio("pick your gender",["male","female"])

# Select Box
st.selectbox("pick your courses",["ML","cloud computing","cyber security"])

# Multi select Box
st.multiselect("Pick your colours",["red","blue","green","red"])

#Creating a slider 
st.select_slider("Rating",["Bad","Average","Good","Outstanding"])

#Slider
st.slider("select your number",0,30)

# pick a number as an input
st.number_input("pick your number",0,100)

# Getting an text input from the user
st.text_input("enter your email address")

# For getting date input from the user
st.date_input("opening ceremony")

#For getting time input from the user
st.time_input("Hey whats the timing")

# Text Area
st.text_area("Write your description about streamlit")

# For uploading a file
st.file_uploader("Upload your files here")

st.color_picker("color")

st.progress(90)

# Spinner
with st.spinner("just wait"):
    t.sleep(5)

#creating a side bar
st.sidebar.title("Prediction app")
st.sidebar.text_input("mail_address")
st.sidebar.text_input("password")
st.sidebar.button("submit")
st.sidebar.radio("professional expert", ["student","working"])


# DATA VISUALIZATION
import pandas as pd
import numpy as np
st.title("bar chart")
data = pd.DataFrame(np.random.randn(50,2),columns = ["x","y"])
st.bar_chart(data)

st.title("Line chart")
st.line_chart(data)

st.title("area chart")
st.area_chart(data)




    







