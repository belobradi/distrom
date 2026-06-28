import os
import streamlit as st
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

@st.cache_resource
def get_db_connection():
    timezone = os.getenv("TIMEZONE", "Europe/Berlin")

    db_url = (
        f'postgresql://{os.getenv("POSTGRES_USER")}:'
        f'{os.getenv("POSTGRES_PASSWORD")}@'
        f'{os.getenv("POSTGRES_HOST")}:'
        f'{os.getenv("POSTGRES_PORT")}/'
        f'{os.getenv("POSTGRES_DB")}'
    )

    return create_engine(
        db_url,
        connect_args={
            "options": f"-c timezone={timezone}"
        }
    )