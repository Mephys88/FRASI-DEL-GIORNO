import streamlit as st
import pandas as pd
import datetime

df = pd.read_excel("frasi.xlsx")

frasi = df.iloc[:, 0].tolist()

oggi = datetime.date.today()

indice = oggi.timetuple().tm_yday % len(frasi)
frase_del_giorno = frasi[indice]

st.markdown(
    """
    <style>
    /* Sfondo con gradient: panna a bianco */
    body {
        background: linear-gradient(to bottom, #FFF8E7, #FFFFFF);
    }
    /* Stile per la frase */
    .frase {
        font-size: 2em;
        font-weight: bold;
        font-style: italic;
        text-align: center;
        margin-top: 20%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(f'<div class="frase">{frase_del_giorno}</div>', unsafe_allow_html=True)