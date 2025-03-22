import streamlit as st
import pandas as pd
import random
from datetime import date

frasi_df = pd.read_excel("frasi.xlsx")
num_frasi = len(frasi_df)
def get_daily_frase():
    random.seed(date.today().toordinal())
    index = random.randint(0, num_frasi - 1)
    return frasi_df.iloc[index, 0]
def get_random_frase():
    index = random.randint(0, num_frasi - 1)
    return frasi_df.iloc[index, 0]
st.set_page_config(page_title="MOTIVATION", page_icon="☠️", layout="centered")
st.markdown(
    """
    <style>
        .big-font {
            font-size: 30px !important;
            font-weight: bold;
            font-style: italic;
            text-align: center;
            color: white;
        }
        .refresh-button {
            display: flex;
            justify-content: center;
        }
        .stButton>button {
            width: 50px;
            height: 50px;
            font-size: 24px;
            border-radius: 50%;
            border: none;
            background-color: #444;
            color: white;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #666;
        }
    </style>
    """,
    unsafe_allow_html=True
)
if "frase" not in st.session_state:
    st.session_state.frase = get_daily_frase()
st.markdown(f"<p class='big-font'>{st.session_state.frase}</p>", unsafe_allow_html=True)
if st.button("♻️"):
    st.session_state.frase = get_random_frase()
    st.rerun()
