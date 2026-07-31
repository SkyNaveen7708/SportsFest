import streamlit as st

st.set_page_config(
    page_title="Teams",
    page_icon="👥",
    layout="wide"
)

# Same padding as Home.py
st.markdown("""
<style>
.block-container {
    padding-top: 0rem;
    padding-bottom: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
}
</style>
""", unsafe_allow_html=True)

# Display image exactly like Home
st.image(
    "assets/teams_page.png",
    use_container_width=True
)