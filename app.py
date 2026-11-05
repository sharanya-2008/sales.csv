
import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Sales Data Analysis Dashboard")

# Read CSV file
df = pd.read_csv("sales.csv")

# Display dataset
st.header("Sales Dataset")
st.dataframe(df)

# Dataset information
st.header("Dataset Information")

st.write("Number of Rows:", df.shape[0])
st.write("Number of Columns:", df.shape[1])

# Summary statistics
st.header("Statistical Summary")
st.write(df.describe())

# Check missing values
st.header("Missing Values")
st.write(df.isnull().sum())

# Sales calculation
# Change these column names if your dataset is different
if "units" in df.columns and "unit_price" in df.columns:
    df["revenue"] = df["units"] * df["unit_price"]

    st.header("Total Revenue")
    st.metric("Revenue", f"₹{df['revenue'].sum():,.2f}")

    # Revenue by category
    if "category" in df.columns:
        st.header("Revenue by Category")

        category_sales = df.groupby("category")["revenue"].sum().reset_index()

        fig = px.bar(
            category_sales,
            x="category",
            y="revenue",
            title="Revenue by Category"
        )

        st.plotly_chart(fig)

    # Revenue by region
    if "region" in df.columns:
        st.header("Revenue by Region")

        region_sales = df.groupby("region")["revenue"].sum().reset_index()

        fig2 = px.pie(
            region_sales,
            names="region",
            values="revenue",
            title="Revenue by Region"
        )

        st.plotly_chart(fig2)
else:
    st.warning("Dataset must contain units and unit_price columns.")
