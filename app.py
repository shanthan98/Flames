import streamlit as st
from flames import calculate_flames

# Page config
st.set_page_config(page_title="FLAMES Calculator", page_icon="🔥")

# 💖 Custom CSS for background + styling
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1509042239860-f550ce710b93");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
    right: 2rem;
}

h1, h2, h3, h4 {
    color: white !important;
    text-align: center;
}

p, label {
    color: white !important;
    font-size: 18px;
}

.stTextInput>div>div>input {
    background-color: rgba(255,255,255,0.8);
    color: black;
    border-radius: 10px;
}

.stButton>button {
    background-color: #ff4b6e;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

.stButton>button:hover {
    background-color: #ff1e4d;
    color: white;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Title
st.title("🔥 FLAMES Calculator ")
st.write("Discover your relationship destiny 💕")

# Inputs
name1 = st.text_input("Enter your name")
name2 = st.text_input("Enter your partner name")

# Button
if st.button("Calculate Love"):
    if name1 and name2:
        try:
            result = calculate_flames(name1, name2)

            st.subheader("Results")
            st.write(f"**Name 1:** {result['name1']} (Length: {result['length1']})")
            st.write(f"**Name 2:** {result['name2']} (Length: {result['length2']})")

            st.success(f"🔥 Relationship: {result['result']} ")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter both names")
