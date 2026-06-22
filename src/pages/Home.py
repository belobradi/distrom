import streamlit as st
import sqlalchemy as sqal
from src.importer.import_network_model import main as run_import

# Database connection
engine = sqal.create_engine('postgresql://postgres:123456@localhost:5432/distrom')

if st.button("Import Network Model"):
    run_import()
