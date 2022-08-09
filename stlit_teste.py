from pickle import TRUE
import streamlit as st
import numpy as np
import pandas as pd
import time

rod = 'Feito por github/jceneziojr'

if st.checkbox('Mostrar primeira seção'):
    x = st.slider('Selecione o valor de x: ', max_value=10)
    df = pd.DataFrame({
        'Coluna 1': [5, 10, 15, 20],
        'Coluna 2': [x*5, x*10, x*15, x*20]
    })

    st.write(x, 'ao quadrado é igual à', x * x)
    st.write(df)

    dataframe = pd.DataFrame(
        #np.random.randn(5, x+1),
        np.random.randint(25, size=(5,x+1)),
        columns=('col %d' % i for i in range(x+1)))

    st.dataframe(dataframe.style.highlight_min(axis=0))
    st.table(dataframe.style.highlight_max(axis=0))

if st.checkbox('Mostrar segunda seção'):
    st.slider('Selecione o valor de x: ', key="y", max_value=10)
    chart_data = pd.DataFrame(
         np.random.randn(st.session_state.y+2, 3),
        columns=['Linha 1', 'Linha 2', 'Linha 3'])
    st.line_chart(chart_data)

if st.checkbox('Mostrar mapa'):
    with st.spinner('Aguarde...'):
        time.sleep(1)
    lat = st.slider('Latitude', min_value=-90.0, max_value=90.0)
    lon = st.slider('Longitude', min_value=-180.0, max_value=180.0)
    mpdt = pd.DataFrame({
    'lat': [lat, -21.1374538],
    'lon': [lon, -44.2652162]})
    st.map(mpdt)


if st.checkbox('Mostrar quarta seção'):
    with st.spinner('Aguarde...'):
        time.sleep(1)
    df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40]
    })

    option = st.selectbox('Escolha um número:', df['c1'])

    'Escolhido: ', option

if st.checkbox('Mostrar sidebar'):
    with st.spinner('Aguarde...'):
        time.sleep(0.5)
    add_selectbox = st.sidebar.selectbox(
        'Forma de contato',
        ('Email', 'Telefone')
    )
    add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
    )


rod
