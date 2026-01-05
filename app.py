# Importações do projeto
import streamlit as st
import pandas as pd
from streamlit import columns
import random

# -- Titulo do Dashboard
st.title("DashBoard - :rainbow[VALE]")
st.balloons()
st.sidebar.markdown("# Porto Norte")
st.sidebar.markdown("### Selecione a Subestação:")

# -- Lateral Esqueda
st.sidebar.text("Descarregamento:")

if st.sidebar.button("SE311KP-D"):
    pass
if st.sidebar.button("SE311KP-E"):
    pass
if st.sidebar.button("SE311KP-F"):
    VV07 = random.randint(18,26)
    VV08 = random.randint(18,26)
    st.write("Temperatura VV07: " + str(VV07) + "ºC\n","\nTemperatura VV08: " + str(VV08) + "ºC")
    st.bar_chart({"VV07": VV07, "VV08": VV08},color="#ff2c2c")

# --------
st.sidebar.text("Embarque:")
st.sidebar.button("SE3xxKP-x1")
st.sidebar.button("SE3xxKP-x2")
st.sidebar.button("SE3xxKP-x3")
st.sidebar.button("SE3xxKP-x4")
st.sidebar.button("SE3xxKP-x5")
st.sidebar.button("SE3xxKP-x6")
st.sidebar.button("SE3xxKP-x7")
