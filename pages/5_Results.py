import streamlit as st
from utils.sheets import read_sheet

# ------------------------------------
# Page Config
# ------------------------------------
st.set_page_config(
    page_title="Results",
    page_icon="🏆",
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
st.title("🏆 Results")
st.caption("Live tournament results")

# ------------------------------------
# Read Google Sheets
# ------------------------------------
matches_df = read_sheet("Matches")
results_df = read_sheet("Results")

# ------------------------------------
# Sport Selector
# ------------------------------------
sports = [
    "Chess",
    "Carrom",
    "Table Tennis",
    "Badminton",
    "Gully Cricket",
    "Foosball",
    "Quiz",
]

selected_sport = st.pills(
    "Select Sport",
    sports,
    selection_mode="single",
    default="Chess"
)

# ------------------------------------
# Filter Matches
# ------------------------------------
game_df = matches_df[matches_df["Game"] == selected_sport]

if game_df.empty:
    st.info(f"No matches available for {selected_sport}.")
else:

    required_columns = [
        "Match No.",
        "Category",
        "Fixture",
        "Match Date",
        "Players",
        "Match Points",
        "Winning Team"
    ]

    for col in required_columns:
        if col not in game_df.columns:
            game_df[col] = ""

    st.dataframe(
        game_df[required_columns],
        use_container_width=True,
        hide_index=True
    )

# ------------------------------------
# Category Winners
# ------------------------------------
game_results = results_df[results_df["Game"] == selected_sport]

if not game_results.empty:

    st.markdown("## 🏅 Category Winners")

    category_df = game_results[
        ["Category", "Winner", "Points"]
    ].copy()

    st.dataframe(
        category_df,
        use_container_width=True,
        hide_index=True
    )

# ------------------------------------
# Overall Winners (Selected Game Only)
# ------------------------------------
game_results = results_df[results_df["Game"] == selected_sport]

overall = (
    game_results["Game Winner"]
    .dropna()
    .astype(str)
)

overall = overall[overall.str.strip() != ""]

if len(overall) > 0:

    st.markdown("## 🏆 Overall Winners")

    medals = ["🥇", "🥈", "🥉"]

    for i, winner in enumerate(overall):
        medal = medals[i] if i < len(medals) else "🏅"
        st.success(f"{medal} {winner}")