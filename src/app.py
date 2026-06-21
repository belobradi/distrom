import streamlit as st

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