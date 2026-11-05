import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv("sales_5000_messy.csv")
st.write(df.head(3))