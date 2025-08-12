from main import expo
import streamlit as st
import asyncio
import time

# Page configuration
st.set_page_config(
    page_title="Thermo Thinker",
    page_icon="⚗️",
    layout="centered",
)

# Custom background color and styling using HTML/CSS
st.markdown("""
    <style>
    body {
        background-color: #000000;
    }
    .header {
        text-align: center;
        font-size: 2.3rem;
        font-weight: bold;
        color: #6cb2e4;
    }
    .footer {
        margin-top: 2rem;
        text-align: center;
        color: #999;
        font-size: 0.85rem;
    }
    </style>
""", unsafe_allow_html=True)

# App header
st.markdown('<div class="header">🧫THERMO🧫 THINKER</div>', unsafe_allow_html=True)

# Chat input
user = st.chat_input("Ask chemical mystery here ...")

if user:
    st.info(f"{user}")

    # Get AI result
    result = asyncio.run(expo(user))

    # Typing effect
    placeholder = st.empty()
    typed_text = ""
    for char in result:
        typed_text += char
        placeholder.markdown(f"{typed_text}▌")  # cursor
        time.sleep(0.01)  # speed

    # Final text (remove cursor)
    placeholder.markdown(f"{typed_text}")

# Footer
st.markdown('<div class="footer">Made with 🧪 by Areeb</div>', unsafe_allow_html=True)
