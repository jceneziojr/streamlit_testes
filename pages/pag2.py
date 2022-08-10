import streamlit as st

rod = 'Feito por github/jceneziojr'

st.title("on_change")

"st.session_state object:", st.session_state

def kmh_p_ms():
    st.session_state.ms = st.session_state.kmh/3.6

def ms_p_kmh():
    st.session_state.kmh = st.session_state.ms*3.6


col1, esp, col2 = st.columns([2,1,2])

with col1:
    ms = st.number_input("m/s", key='ms', on_change= ms_p_kmh)

with col2:
        kh = st.number_input("km/h", key='kmh', on_change= kmh_p_ms)


rod