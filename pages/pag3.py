from ast import If
import streamlit as st
import datetime

st.title('Exemplos úteis da documentação')

if st.checkbox('session states'):

    if 'count2' not in st.session_state:
        st.session_state.count2 = 0
        st.session_state.last_updated = datetime.time(0,0)

    st.session_state

    def update_counter():
        st.session_state.count2 += st.session_state.increment_value
        st.session_state.last_updated = st.session_state.update_time

    with st.form(key='my_form'):
        st.time_input(label='Enter the time', value=datetime.datetime.now().time(), key='update_time')
        st.number_input('Enter a value', value=0, step=1, key='increment_value')
        submit = st.form_submit_button(label='Update', on_click=update_counter)

    st.write('Current Count = ', st.session_state.count2)
    st.write('Last Updated = ', st.session_state.last_updated)

if st.checkbox('tabs'):
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)