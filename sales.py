import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv("sales_5000_messy.csv")
print(df.head(3))
print(df.head(3))
print("df.types")
df["revenue" ] = df["units"] *df["unit_price"]
print(df["revenue"].sum())


import streamlit as st
REQ = {"oder_id","date","region","category","units","unit_price"}
f = st.file_uploader("upload CSV",type ="csv")
if f is not None:
    try:
        df = pd.read_csv(f)
        missing = REQ -set(df.columns)
        if missing:
            st.error(f"missing column:{missing}")
        else:
            st.success("csv file upload successfully")
            st.dataframe(df.head())
    except Exception as e:
          st.error(f"error reading csv:{e}")




df["date"] = pd.to_datetime(df["date"])
df["revenue"] = df["units"]*df["unit_price"]
daily = df.groupby("date",as_index=False)["revenue"].sum()
fig = px.line(daily,x="date",y ="revenue",markers=True,title = "daily revenue")
st.plotly_chart(fig)