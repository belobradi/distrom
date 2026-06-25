import streamlit as st
import pandas as pd
from db_utils import get_db_connection

engine = get_db_connection()

st.title("Logs Viewer")

df = pd.read_sql(f"SELECT * FROM public.execution_logs_v", engine)
st.dataframe(df, use_container_width=True)