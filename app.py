import streamlit as st
from sheets import save_to_sheet
from flames import calculate_flames

# -----------------------------------
# 🧹 Clear Input Function
# -----------------------------------
def clear_inputs():
    st.session_state["name1"] = ""
    st.session_state["name2"] = ""

# -----------------------------------
# 🔥 Page Configuration
# -----------------------------------
st.set_page_config(page_title="FLAMES Calculator", page_icon="❤️")

# -----------------------------------
# 🎨 Custom CSS Styling (UI + Background)
# -----------------------------------
page_bg = """
<style>

/* Background with dark overlay */
[data-testid="stAppViewContainer"] {
    background-image: 
        linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)),
        url("https://images.unsplash.com/photo-1509042239860-f550ce710b93");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Remove header */
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* Center container */
.main > div {
    max-width: 900px;
    margin: auto;
    background: rgba(0, 0, 0, 0.65);
    padding: 2.5rem;
    border-radius: 20px;
    box-shadow: 0px 0px 25px rgba(0,0,0,0.6);
}

/* Title */
h1 {
    color: #ffccd5 !important;
    text-align: center;
    font-size: 2.8rem;
    font-weight: bold;
}

/* Subtitle */
p {
    color: #f1f1f1 !important;
    text-align: center;
}

/* Labels */
label {
    color: #ffd6e0 !important;
    font-weight: 500;
}

/* Input fields */
.stTextInput>div>div>input {
    background-color: rgba(255,255,255,0.95);
    color: black;
    border-radius: 12px;
    padding: 10px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(45deg, #ff4b6e, #ff758f);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
    border: none;
}

/* Button hover */
.stButton>button:hover {
    background: linear-gradient(45deg, #ff1e4d, #ff4b6e);
}

/* Results */
h3 {
    color: #ffe5ec !important;
    text-align: center;
}

/* Success box */
.stSuccess {
    background-color: rgba(255, 75, 110, 0.25) !important;
    color: white !important;
    border-radius: 10px;
}

</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# -----------------------------------
# 🏷️ Title Section
# -----------------------------------
st.markdown("""
    <div style="text-align:center; margin-top:20px;">
        <h1>FLAMES Calculator</h1>
        <p>Discover your relationship destiny 💕</p>
    </div>
""", unsafe_allow_html=True)

# -----------------------------------
# 🧱 Layout: Inputs + Legend
# -----------------------------------
left_col, right_col = st.columns([3, 1], gap="large")

# -----------------------------------
# 📝 LEFT SIDE → Inputs + Buttons
# -----------------------------------
with left_col:

    name1 = st.text_input("Enter your name", key="name1")
    name2 = st.text_input("Enter your partner name", key="name2")

    col1, col2, col3 = st.columns([1, 1, 3])

    with col1:
        calculate_clicked = st.button("Calculate Love")

    with col2:
        st.button("Clear", on_click=clear_inputs)

# -----------------------------------
# 📦 RIGHT SIDE → FLAMES Legend
# -----------------------------------
with right_col:
    st.markdown("""
    <div style="
        margin-top: 10px;
        background: rgba(0, 0, 0, 0.65);
        padding: 20px;
        border-radius: 15px;
        color: #ffd6e0;
        font-size: 14px;
        box-shadow: 0px 0px 12px rgba(0,0,0,0.5);
    ">
        <h4 style="text-align:center;">❤️ FLAMES</h4>
        <hr style="border: 0.5px solid #ffccd5;">
        F → Friends<br>
        L → Lovers<br>
        A → Affection<br>
        M → Marriage<br>
        E → Enemies<br>
        S → Siblings
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------
# ❤️ Calculate Logic
# -----------------------------------
if calculate_clicked:
    if name1 and name2:
        try:
            result = calculate_flames(name1, name2)

            st.subheader("Results")
            st.write(f"**Name 1:** {result['name1']} (Length: {result['length1']})")
            st.write(f"**Name 2:** {result['name2']} (Length: {result['length2']})")

            st.success(f"Relationship: {result['result']}")

            # Save to Google Sheets
            save_to_sheet(result)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter both names")
        
# ----------- FOOTER SECTION -----------

st.markdown("---")

st.markdown(
"""
<div style="text-align:center; margin-top:30px; color:#ffd6e0;">

<p style="font-size:18px; margin-bottom:12px;">Find me on</p>

<div style="display:flex; justify-content:center; gap:30px; margin-bottom:20px;">

<a href="https://github.com/shanthan98" target="_blank">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"
     width="32"
     style="filter: brightness(0) invert(1); transition: 0.3s;">
</a>

<a href="https://www.linkedin.com/in/shanthan-k/" target="_blank">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="32">
</a>

<a href="https://shanthan-kasula-portfolio.netlify.app/" target="_blank">
<img src="https://cdn-icons-png.flaticon.com/512/1006/1006771.png"
     width="32"
     style="filter: brightness(0) invert(1); transition: 0.3s;">
</a>

</div>

<div style="margin-bottom:15px;">
<img src="https://hitwebcounter.com/counter/counter.php?page=21484220&style=0011&nbdigits=5&type=page&initCount=42" title="Free Tools" Alt="Free Tools"   border="0"/>
</div>

<p style="font-size:14px; color:#ffccd5;">
Copyrights ©2026 All rights reserved | Made with ❤️ by Shanthan
</p>

</div>
""",
unsafe_allow_html=True
)
