import streamlit as st 
import duckdb 

results = duckdb.sql("SELECT 42").df()
st.write('results')
