import streamlit as st

st.set_page_config(
    page_title="Fixtures",
    page_icon="📅",
    layout="wide"
)

# -----------------------------
# Page Styling
# -----------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.title("📅 Fixtures")

st.write("")

# Chess & Quiz Fixtures
st.image(
    "assets/fixtures/chess&quiz.png",
    width=900
)

st.write("")
st.write("")

# Other Sports Fixtures
st.image(
    "assets/fixtures/others.png",
    width=900
)