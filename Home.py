import streamlit as st

st.set_page_config(
    page_title="QA Champions Cup 2026",
    page_icon="🏆",
    layout="wide"
)

# Remove top padding and reduce side padding
st.markdown("""
<style>
.block-container {
    padding-top: 0.5rem;
    padding-bottom: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
}
</style>
""", unsafe_allow_html=True)

# Sports Collage
st.image(
    "assets/sports_collage.png",
    use_container_width=True
)