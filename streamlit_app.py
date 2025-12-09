import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
st.set_page_config(
    page_title="¿Estás en forma? - Clasificador",
    page_icon="🏃‍♀️",
    layout="centered"
