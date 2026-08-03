import streamlit as st
from utils.sheets import read_sheet

st.set_page_config(
    page_title="Results",
    page_icon="🏆",
    layout="wide"
)

# ------------------------------------
# Page Styling
# ------------------------------------
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
st.title("🏆 Results")
st.caption("Live tournament results")

st.markdown("---")

# ------------------------------------
# Read Google Sheet
# ------------------------------------
df = read_sheet("Matches")

# ------------------------------------
# Display Results
# ------------------------------------
if df.empty:
    st.info("No match data available.")
else:

    display_df = df[
        [
            "Match No.",
            "Game",
            "Category",
            "Fixture",
            "Match Date",
            "Players",
            "Match Points",
            "Winning Team"
        ]
    ]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )