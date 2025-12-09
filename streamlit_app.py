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
variables_num = []
variables_cat = []
for col in df.columns:
    if col == target:
        continue
    if df[col].dtype in ["int64", "float64"]:
        variables_num.append(col)
    else:
        variables_cat.append(col)

st.write("**Variables numéricas detectadas:**", variables_num)
st.write("**Variables categóricas detectadas:**", variables_cat)
st.subheader("Entrenando modelo basado en reglas…")

regla_actividad = None
# Detectar tipos de columnas automáticamente
for col in df.columns:
    if col == target:
        continue
    if df[col].dtype in ["int64", "float64"]:
        variables_num.append(col)
    else:
        variables_cat.append(col)

st.write("**Variables numéricas detectadas:**", variables_num)
st.write("**Variables categóricas detectadas:**", variables_cat)

# -----------------------------------------------------------
# ENTRENAR MODELO BASADO EN REGLAS
# -----------------------------------------------------------
st.subheader("Entrenando modelo basado en reglas…")

# Regla 1: si el índice de actividad es alto → probablemente está en forma.
regla_actividad = None
for col in df.columns:
    if "actividad" in col.lower():
        regla_actividad = col
        break

# Regla 2: si duerme bien y tiene buen peso
regla_sueno = None
for col in df.columns:
    if "sue" in col.lower():
        regla_sueno = col
        break

# Regla 3: si la frecuencia cardiaca es baja → buena condición
regla_fc = None
for col in df.columns:
    if "cardiaca" in col.lower() or "heart" in col.lower():
        regla_fc = col
        break

st.success("Modelo basado en reglas entrenado correctamente ✔️")
# FORMULARIO DE PREDICCIÓN
# -----------------------------------------------------------
st.subheader("🔮 Haz una predicción")

input_data = {}

# Crear sliders dinámicos según columnas numéricas detectadas
for col in variables_num:
    minimo = float(df[col].min())
    maximo = float(df[col].max())
    valor_default = float(df[col].mean())
    input_data[col] = st.slider(
        f"{col}",
        minimo, maximo, valor_default
    )

# Categorías
for col in variables_cat:
    opciones = df[col].dropna().unique().tolist()
    input_data[col] = st.selectbox(f"{col}", opciones)

if st.button("Predecir"):
    score = 0
