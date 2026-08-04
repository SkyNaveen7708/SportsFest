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
# Sports Selector
# ------------------------------------
games = [
    ("♟", "Chess"),
    ("🪙", "Carrom"),
    ("🏓", "Table Tennis"),
    ("🏸", "Badminton"),
    ("🏏", "Gully Cricket"),
    ("⚽", "Foosball"),
    ("❓", "Quiz"),
]

st.write("### Select Sport")

cols = st.columns(len(games))

if "selected_game" not in st.session_state:
    st.session_state.selected_game = "Chess"

for i, (icon, game) in enumerate(games):
    with cols[i]:
        if st.button(
            f"{icon} {game}",
            use_container_width=True,
            type="primary" if st.session_state.selected_game == game else "secondary",
        ):
            st.session_state.selected_game = game

selected = st.session_state.selected_game

# ------------------------------------
# Match Results
# ------------------------------------
match_df = matches_df[matches_df["Game"] == selected]

st.markdown("## 📋 Match Results")

if match_df.empty:
    st.info(f"No matches available for {selected}.")
else:

    display_df = match_df[
        [
            "Match No.",
            "Category",
            "Fixture",
            "Match Date",
            "Players",
            "Match Points",
            "Winning Team",
        ]
    ]

    st.dataframe(
        display_df,
        width="stretch",
        hide_index=True,
    )

# ------------------------------------
# Category Winners
# ------------------------------------
st.markdown("## 🏅 Category Winners")

game_results = results_df[results_df["Game"] == selected]

if game_results.empty:
    st.info("Category winners not updated yet.")

else:

    winners_df = game_results[
        [
            "Category",
            "Winner",
            "Points",
        ]
    ]

    st.dataframe(
        winners_df,
        width="stretch",
        hide_index=True,
    )

# ------------------------------------
# Overall Winner
# ------------------------------------
overall = (
    game_results["Game Winner"]
    .dropna()
    .astype(str)
)

overall = overall[overall.str.strip() != ""]

if len(overall):

    st.markdown("## 🏆 Overall Winner")

    st.success(
        f"🥇 {overall.iloc[0]}"
    )