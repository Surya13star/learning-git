import pandas as pd
import streamlit as st


def lbs_to_kgs():
    st.session_state["kgs"] = st.session_state["lbs"]/2.2046

def kgs_to_lbs():
    st.session_state["lbs"] = st.session_state["kgs"]*2.2046

st.title('Session States')

if "a_counter" not in st.session_state:
    st.session_state['a_counter'] = 0

if "boolean" not in st.session_state:
    st.session_state['boolean']= False
st.write(st.session_state)

st.write('session_state: a_counter is',st.session_state["a_counter"])
st.write('session_state: boolean is', st.session_state["boolean"])

for keys in st.session_state.keys():
    st.write(keys)

for item in st.session_state.items():
    item

button = st.button('increase counter')

if button:
    st.session_state["a_counter"] += 1

st.write(st.session_state["a_counter"])

col1, col2, col3 = st.columns([2,2,2])
with col1:
    pounds = st.number_input("pounds :", key = "lbs", on_change = lbs_to_kgs)

with col3:
    kilograms = st.number_input("kilograms :", key = "kgs", on_change = kgs_to_lbs)

