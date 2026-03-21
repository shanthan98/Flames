import streamlit as st
from flames import calculate_flames

# Page title
st.set_page_config(page_title="FLAMES Calculator", page_icon="🔥")

st.title(" FLAMES Calculator")
st.write("Find your relationship status using the classic FLAMES game!")

# Input fields
name1 = st.text_input("Enter your name")
name2 = st.text_input("Enter your partner name")

# Button
if st.button("Calculate"):
    if name1 and name2:
        try:
            result = calculate_flames(name1, name2)

            st.subheader(" Results")
            st.write(f"**Name 1:** {result['name1']} (Length: {result['length1']})")
            st.write(f"**Name 2:** {result['name2']} (Length: {result['length2']})")

            st.success(f" Relationship: {result['result']}")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter both names.")
