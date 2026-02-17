nda-reviewer.pyimport streamlit as st

st.title("NDA Reviewer Ninja")

text = st.text_area("Paste the contract here:", height=300)

if st.button("Review"):
    if not text.strip():
        st.warning("Nothing to check!")
    else:
        keywords = ["confidential", "proprietary", "non-disclosure", "trade secret", "restricted"]
        found = if found:
            st.error(f"Uh-oh—found these red flags: {', '.join(found)}")
        else:
            st.success("Looks clean! No big NDA traps spotted."
