import streamlit as st
from src.importer.import_network_model import main as run_import

if st.button("Import Network Model"):
    run_import()
