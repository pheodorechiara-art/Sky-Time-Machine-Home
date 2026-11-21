import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Sky Time Machine", layout="wide", initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
      header, footer, #MainMenu {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("landing.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)