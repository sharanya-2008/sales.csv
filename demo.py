import pandas as pd
import plotly.express as px
import streamlit as st

# read the csv file
df = pd.read_csv("sales.csv")

# Convert date column into datetime
df["date"] = pd.to_datetime(df["date"])

# Calculate revenue
df["revenue"] = df["units"] * df["unit_price"]

# Revenue by category
by_cat = df.groupby("category", as_index=False)["revenue"].sum()

# Bar chart
fig = px.bar(
    by_cat,
    x="category",
    y="revenue",
    title="Revenue by Category (Jan 2026)"
)

st.plotly_chart(fig)

# Daily revenue
daily = df.groupby("date", as_index=False)["revenue"].sum()

# Line chart
fig = px.line(
    daily,
    x="date",
    y="revenue",
    markers=True,
    title="Daily Revenue"
)

st.plotly_chart(fig)