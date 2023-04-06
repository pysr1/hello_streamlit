import streamlit as st 
import duckdb 

duckdb.sql("INSTALL httpfs; LOAD httpfs")
results = duckdb.sql("SELECT * FROM read_csv_auto('https://raw.githubusercontent.com/pysr1/jaffle_shop/main/seeds/raw_orders.csv'").df()
st.write(results.head(10))
