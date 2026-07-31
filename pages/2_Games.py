import streamlit as st
from utils.sheets import read_sheet

st.set_page_config(
    page_title="Games",
    page_icon="🎮",
    layout="wide"
)

# ------------------------------------
# Page Styling
# ------------------------------------
st.markdown("""
<style>
.block-container{
    padding-top:0.8rem;
    padding-left:2rem;
    padding-right:2rem;
    padding-bottom:1rem;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------
# Sports
# ------------------------------------
sports = [
    "♟ Chess",
    "🪙 Carrom",
    "🏓 Table Tennis",
    "🏸 Badminton",
    "🏏 Gully Cricket",
    "⚽ Foosball",
    "❓ Quiz"
]

# ------------------------------------
# Sport Selector
# ------------------------------------

# Space above the selector
st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)


selected = st.pills(
    "Select Sport",
    sports,
    default="♟ Chess"
)

st.write("")

# Remove emoji to match Google Sheet
selected_sport = selected.split(" ", 1)[1]

# ------------------------------------
# Read Rules
# ------------------------------------
df = read_sheet("Games")
rules = df[df["Sport"] == selected_sport]

# ------------------------------------
# Image Name
# ------------------------------------
image_name = selected_sport.lower().replace(" ", "_")

# ------------------------------------
# Layout
# ------------------------------------
left, right = st.columns([1, 1.1], gap="large")

with left:
    st.image(
        f"assets/games/{image_name}.png",
        width=520
    )

with right:

    st.markdown(f"### 📋 {selected} Rules")

    if rules.empty:
        st.info("Rules not added yet.")
    else:
        for _, row in rules.iterrows():
            st.markdown(f"✅ {row['Rule']}")