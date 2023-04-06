#import streamlit as st 
#import duckdb 

#duckdb.sql("INSTALL httpfs; LOAD httpfs")
#results = duckdb.sql("SELECT user_id, max(order_date)  FROM read_csv_auto('https://raw.githubusercontent.com/pysr1/jaffle_shop/main/seeds/raw_orders.csv') group by all").df()
#st.write(results.head(10))

import streamlit as st
import pandas as pd
import numpy as np

# Create a title for the app
st.title("Bar Chart Example")

# Create some sample data
data = {'apples': 10, 'oranges': 15, 'bananas': 5}
df = pd.DataFrame(list(data.items()), columns=['Fruit', 'Count'])

# Create a bar chart using the native streamlit plotting library
fig = (
    df.plot(kind='bar', x='Fruit', y='Count')
    .figure
)

# Display the chart
st.write(fig)
