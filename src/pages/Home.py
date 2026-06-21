import subprocess
import streamlit as st

if st.button("Import Network Model"):
    result = subprocess.run(["python", "./src/import_network_model.py"], capture_output=True, text=True)
    st.text(result.stdout)