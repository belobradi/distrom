import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.set_page_config(
    page_title="Distrom",
    page_icon=":zap:",
    layout="wide",
)

pg = st.navigation(
    [
        st.Page("pages/Home.py", title="Home", icon="🏠", default=True),
        st.Page("pages/Parameters.py", title="Parameters", icon="⚙"),
        st.Page("pages/Logs.py", title="Logs", icon="📜"),
    ]
)
pg.run()