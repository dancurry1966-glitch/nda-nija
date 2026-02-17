nda_ninja.py
if st.session_state.signed:
    # Ninja throw sequence
    with st.empty():
        st.markdown("🌀 *whoosh!* 🌀")
        time.sleep(0.5)  # tiny pause for drama
        
        st.markdown("💥 *shuriken hits!* 💥")
        time.sleep(0.8)
    
    # Redacted stamp reveal
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
    
    # Bonus: confetti + sound (if browser allows)
    st.balloons()
    # st.audio("https://www.soundjay.com/buttons/button-3.mp3", format="mp3")  # optional, swap with real ninja sound
