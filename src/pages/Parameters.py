import streamlit as st
import pandas as pd
import sqlalchemy as sqal

engine = sqal.create_engine('postgresql://postgres:123456@localhost:5432/distrom')

st.title("Distrom - Network Data Viewer")

query_tables = sqal.text("SELECT tablename FROM pg_catalog.pg_tables WHERE tablename LIKE 'source_%';")
tables = pd.read_sql(query_tables, engine.connect())['tablename'].tolist()

selected_table = st.selectbox("Choose table:", tables)

if selected_table:
    df = pd.read_sql(f"SELECT * FROM {selected_table}", engine)
    
    st.write(f"Table: **{selected_table}**")
    st.dataframe(df, use_container_width=True)
