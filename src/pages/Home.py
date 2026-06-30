import streamlit as st
from importer.initialize_source import main as run_import
from src.common.db_utils import get_db_connection
from sqlalchemy import text

engine = get_db_connection()


# Set up the Streamlit page layout
if "status" not in st.session_state:
    st.session_state.status = "Idle"

col, spacer = st.columns([1, 3])
with col:
    if st.button("Update Source", width='stretch'):
        run_import()

col, spacer = st.columns([1, 3])
with col:
    if st.button("Initialize", width='stretch'):
        with engine.begin() as conn:
            conn.execute(text("SELECT fnc.import_network()"))
