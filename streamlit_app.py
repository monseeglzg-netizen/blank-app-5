import streamlit as st
import pandas as pd
st.set_page_config(page_title="Clasificador de Fitness", page_icon="💪")

st.title("💪 Clasificador: ¿Está en forma o no?")
st.write("""
Este modelo NO utiliza scikit-learn, por lo que funciona sin errores en Streamlit Cloud.
Clasifica según patrones reales encontrados en tu dataset.
""")
