import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Sky Time Machine", layout="wide", initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
      header, footer, #MainMenu, [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none !important;}
      .stApp, [data-testid="stAppViewContainer"] {background: #04050c !important;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stVerticalBlock"] {gap: 0 !important;}
      iframe {height: 100vh !important; display: block; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("landing.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)
