import streamlit as st 
import duckdb 

duckdb.sql("INSTALL httpfs; LOAD httpfs")
results = duckdb.sql("SELECT * FROM read_csv_auto('https://data.seattle.gov/api/views/2z5v-ecg8/rows.csv?accessType=DOWNLOAD')").df()
st.write(results.head(10))
