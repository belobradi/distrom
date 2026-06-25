import os
import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

@st.cache_resource
def get_db_connection():
    db_url = f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("POSTGRES_HOST")}:{os.getenv("POSTGRES_PORT")}/{os.getenv("POSTGRES_DB")}'
    return create_engine(db_url)