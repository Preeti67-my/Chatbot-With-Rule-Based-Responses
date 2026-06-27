import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide", page_title="Chatbot Hub", page_icon="🤖")

import home
import rule_based_chatbot

st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    typing_animation = """
    <h3 style="text-align:left;">
    🤖 Chatbot Hub
    </h3>
    """
    st.markdown(typing_animation, unsafe_allow_html=True)

    app = option_menu(
        menu_title="Sections",
        options=["Home", "Rule-Based Chatbot"],
        default_index=0,
    )

if app == "Home":
    home.app()

elif app == "Rule-Based Chatbot":
    rule_based_chatbot.app()