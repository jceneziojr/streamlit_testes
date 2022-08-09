import streamlit as st
import numpy as np
import time

rod = 'Feito por github/jceneziojr'

st.markdown("# Segunda página ❄️")

if st.checkbox('Mostrar columns'):
    with st.spinner('Aguarde...'):
        time.sleep(1)
        st.success('Concluído!')
    c1, c2, c3, c4 = st.columns(4)
    c1.button('Pressione!')

    with c2:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")
    
    with c3:
        val = st.slider('Escolha um valor', 1, 3)
        if val == 1:
            st.image("https://static.streamlit.io/examples/dog.jpg")
            'Cachorro'
        elif val == 2:
            st.image("https://static.streamlit.io/examples/cat.jpg")
            'Gato'
        else:
            st.image("https://static.streamlit.io/examples/owl.jpg")
            'Coruja'

    with c4:
        val1 = st.slider('Escolha um valor', 0.0, 1.0)

if st.checkbox('Mais algumas colunas'):
    col1, col2, col3, col4 = st.columns([3, 1, 2, 1]) #a primeira coluna é 3x maior q a segunda, e pelo jeito, o restante segue sendo proporcional a segunda
    data = np.random.randn(10, 1)

    col1.subheader("Coluna 1")
    col1.line_chart(data)

    col2.subheader("Coluna 2")
    col2.write(data)

    col3.subheader("Coluna 3")
    col3.write(data)

    col4.subheader("Coluna 4")
    col4.write(data)

if st.checkbox('Mostrar "expanders"'):
    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

    with st.expander("Expander"):
        st.write("""
            Nada de mais, apenas foto de um dado
        """)
        st.image("https://static.streamlit.io/examples/dice.jpg")

if st.checkbox('Objeto progress'):
    'Starting a long computation...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.001)
    st.error('This is an error')
    st.warning('This is a warning')
    st.info('This is a purely informational message')
    '...and now we\'re done!'

st.file_uploader('abrir')


rod