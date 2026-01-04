import streamlit as st

st.title("DashBoard")
st.sidebar.markdown("# Porto Norte")
st.sidebar.markdown("### Selecione a Subestação:")

# Lateral Esqueda
st.sidebar.text("Descarregamento:")
st.sidebar.button("SE311KP-D")
st.sidebar.button("SE311KP-E")
st.sidebar.button("SE311KP-F")
# --------
st.sidebar.text("Embarque:")
st.sidebar.button("SE3xxKP-x1")
st.sidebar.button("SE3xxKP-x2")
st.sidebar.button("SE3xxKP-x3")
st.sidebar.button("SE3xxKP-x4")
st.sidebar.button("SE3xxKP-x5")
st.sidebar.button("SE3xxKP-x6")
st.sidebar.button("SE3xxKP-x7")
