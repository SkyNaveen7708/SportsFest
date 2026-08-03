import streamlit as st
from utils.sheets import read_sheet

# ------------------------------------
# Page Config
# ------------------------------------
st.set_page_config(
    page_title="Points Table",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.block-container{
    padding-top:2rem;
    padding-left:2rem;
    padding-right:2rem;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------
# Title
# ------------------------------------
st.title("📊 Points Table")
st.caption("Current tournament standings")

st.divider()

# ------------------------------------
# Read Google Sheet
# ------------------------------------
df = read_sheet("Points Table")

# ------------------------------------
# Display
# ------------------------------------
if df.empty:
    st.info("Points table is not available yet.")
else:
    display_df = df[
        [
            "Game",
            "Winner",
            "Runner Up",
            "2nd Runner Up",
            "Rampage Aquad",
            "Noob Masters",
            "Zero Practise Club"
        ]
    ]

    st.dataframe(
        display_df,
        width="stretch",
        hide_index=True
    )