import streamlit as st 
import duckdb 

results = duckdb.sql("SELECT range(1, 100)").df()
st.write(results)
