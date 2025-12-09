import streamlit as st
import pandas as pd
st.set_page_config(page_title="Clasificador de Fitness", page_icon="💪")

st.title("💪 Clasificador: ¿Está en forma o no?")
st.write("""
Este modelo NO utiliza scikit-learn, por lo que funciona sin errores en Streamlit Cloud.
Clasifica según patrones reales encontrados en tu dataset.
""")
file = st.file_uploader("Sube tu archivo Fitness_Classification.csv", type=["csv"])

if file is None:
    st.info("Sube el archivo para continuar.")
    st.stop()

df = pd.read_csv(file)
st.subheader("Vista rápida del dataset")
st.dataframe(df.head())
target = None
for c in ["is_fit", "esta_en_forma", "está_en_forma"]:
    if c in df.columns:
        target = c
        break

if target is None:
    st.error("No encontré la columna objetivo (`is_fit` o `esta_en_forma`).")
    st.stop()
