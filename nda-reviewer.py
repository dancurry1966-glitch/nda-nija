import streamlit as st
import time

st.set_page_config(page_title="NDA-Ninja", layout="wide")

st.title("NDA-Ninja ⚔️")
st.markdown("Sign. Seal. Stay silent.")

# Sidebar for ninja vibe
with st.sidebar:
    st.image("https://via.placeholder.com/150/000000/FFFFFF?text=Ninja", width=100)
    st.write("Ready to redact? 👀")

# Session state to track if we've "signed"
if "signed" not in st.session_state:
    st.session_state.signed = False

col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Your NDA Text")
    nda_text = st.text_area("Paste the full NDA here...", height=300, 
                            placeholder="This is where the legalese goes...")

    if st.button("Sign with Ninja Seal", type="primary", disabled=not nda_text.strip()):
        st.session_state.signed = True
        
        # Ninja animation sequence
        with st.empty():
            st.markdown("🌀 *whoosh!* 🌀")
            time.sleep(0.5)  # drama pause
            st.markdown("💥 *shuriken hits!* 💥")
            time.sleep(0.8)
        
        # Redacted stamp
        st.markdown(
            """
            <div style="text-align: center; font-size: 80px; color: #ff0000; font-weight: bold; 
                        text-shadow: 3px 3px 5px #000; transform: rotate(-15deg);">
                REDACTED
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        st.success("NDA sealed. Ninja approves. 🥷")
        st.balloons()

# Reset button (optional)
if st.button("Start Over"):
    st.session_state.signed = False
    st.rerun()
