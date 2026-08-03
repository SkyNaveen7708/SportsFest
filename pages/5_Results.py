import streamlit as st
from utils.sheets import read_sheet

st.set_page_config(
    page_title="Results",
    page_icon="🏆",
    layout="wide"
)

# ------------------------------------
# Page Style
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
st.caption("Completed match results")

st.markdown("---")

# ------------------------------------
# Read Google Sheet
# ------------------------------------
df = read_sheet("Matches")

# ------------------------------------
# Show only completed matches
# (WinningTeam is filled)
# ------------------------------------
results = df[df["WinningTeam"].astype(str).str.strip() != ""]

if results.empty:
    st.info("No match results available yet.")
else:

    display_df = results[
        [
            "Match No.",
            "Game",
            "Category",
            "Fixture",
            "Players",
            "Match Points",
            "WinningTeam"
        ]
    ]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )