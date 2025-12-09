import streamlit as st
import pandas as pd

st.set_page_config(page_title="Clasificador Fitness", page_icon="💪")

st.title("💪 Clasificador: ¿Está en forma o no?")
st.write("Este modelo funciona sin sklearn y es totalmente compatible con Streamlit Cloud.")

# ------------------------------
# SUBIR ARCHIVO CSV
# ------------------------------
file = st.file_uploader("Sube el archivo Fitness_Classification.csv", type=["csv"])

if file is None:
    st.info("Sube el archivo para continuar.")
    st.stop()

df = pd.read_csv(file)

st.subheader("Vista del dataset")
st.dataframe(df.head())

# ------------------------------
# DETECTAR VARIABLE OBJETIVO
# ------------------------------
target = None
for col in ["is_fit", "esta_en_forma", "está_en_forma"]:
    if col in df.columns:
        target = col
        break

if target is None:
    st.error("No encontré la columna objetivo (is_fit o está_en_forma).")
    st.stop()

# ------------------------------
# DETECTAR VARIABLES NUMÉRICAS Y CATEGÓRICAS
# ------------------------------
variables_num = [c for c in df.columns if df[c].dtype != "object" and c != target]
variables_cat = [c for c in df.columns if df[c].dtype == "object"]

st.write("Variables numéricas:", variables_num)
st.write("Variables categóricas:", variables_cat)

# ------------------------------
# FORMULARIO DE PREDICCIÓN
# ------------------------------
st.subheader("🔮 Haz una predicción nueva")

input_data = {}

# Crear una clave única para cada slider usando enumerate
for idx, col in enumerate(variables_num):
    minimo = float(df[col].min())
    maximo = float(df[col].max())
    valor_default = float(df[col].mean())

    input_data[col] = st.slider(
        f"{col}",
        minimo,
        maximo,
        valor_default,
        key=f"slider_{idx}"   # ← ID ÚNICO
    )

# Categóricas con claves únicas
for idx, col in enumerate(variables_cat):
    opciones = df[col].dropna().unique().tolist()
    input_data[col] = st.selectbox(
        f"{col}",
        opciones,
        key=f"select_{idx}"  # ← ID ÚNICO
    )

# ------------------------------
# MODELO BASADO EN REGLAS
# ------------------------------

if st.button("Predecir", key="predict_btn"):
    score = 0
    
    # Regla: índice de actividad
    col_act = [c for c in df.columns if "actividad" in c.lower()]
    if col_act:
        col = col_act[0]
        if input_data[col] >= df[col].mean():
            score += 1

    # Regla: horas de sueño
    col_sleep = [c for c in df.columns if "sue" in c.lower()]
    if col_sleep:
        col = col_sleep[0]
        if input_data[col] >= df[col].mean():
            score += 1

    # Regla: frecuencia cardíaca
    col_fc = [c for c in df.columns if "cardiaca" in c.lower()]
    if col_fc:
        col = col_fc[0]
        if input_data[col] <= df[col].mean():
            score += 1

    # --------------------------
    # RESULTADO
    # --------------------------
    st.subheader("Resultado de la predicción")

    if score >= 2:
        st.success("✅ La persona probablemente **SÍ está en forma** (1)")
    else:
        st.warning("⚠️ La persona **NO está en forma** (0)")
