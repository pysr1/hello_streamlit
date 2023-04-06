import streamlit as st 
import duckdb 

duckdb.sql("INSTALL httpfs; LOAD httpfs")
results = duckdb.sql("SELECT * FROM 'hello world'").df()
st.write(results.head(10))
